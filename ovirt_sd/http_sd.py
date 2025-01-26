"""
oVirt HTTP Service Discovery
"""

import os
from typing import List, Dict

import uvicorn
from fastapi import FastAPI, Response, Depends, status
import ovirtsdk4 as sdk
import pydantic

from ovirt_sd.discovery import HostsServiceDiscovery, VMServiceDiscovery


app = FastAPI(title="oVirt Service Discovery", docs_url="/")


class TargetsGroup(pydantic.BaseModel):
    targets: List[str]
    labels: Dict[str, str]


def get_engine_connection():
    """Get connection from env"""
    conn = sdk.Connection(
        url=os.environ.get("OVIRT_URL"),
        username=os.environ.get("OVIRT_USERNAME"),
        password=os.environ.get("OVIRT_PASSWORD"),
        insecure=bool(os.environ.get("OVIRT_INSECURE", False)),
        timeout=int(os.environ.get("OVIRT_SD_TIMEOUT", 60)),
    )
    try:
        yield conn
    finally:
        conn.close()


@app.get("/hosts", response_model=List[TargetsGroup], status_code=status.HTTP_200_OK)
async def get_hosts_targets(
    response: Response, conn: sdk.Connection = Depends(get_engine_connection)
):
    """Get hosts targets endpoint"""
    targets_groups = HostsServiceDiscovery(conn).get_targets_group()
    if not targets_groups:
        response.status_code = status.HTTP_204_NO_CONTENT
    return targets_groups


@app.get("/vms", response_model=List[TargetsGroup], status_code=status.HTTP_200_OK)
async def get_vms_targets(
    response: Response, conn: sdk.Connection = Depends(get_engine_connection)
):
    """Get virtual machines targets endpoint"""
    targets_groups = VMServiceDiscovery(conn).get_targets_group()
    if not targets_groups:
        response.status_code = status.HTTP_204_NO_CONTENT
    return targets_groups


def main():
    """Main HTTP"""
    uvicorn.run(app, port=int(os.environ.get("OVIRT_SD_PORT")))
