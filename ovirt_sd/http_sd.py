"""
oVirt HTTP Service Discovery
"""
import os

import uvicorn
from fastapi import FastAPI, Depends
import ovirtsdk4 as sdk

from ovirt_sd.discovery import HostsServiceDiscovery, VMServiceDiscovery


app = FastAPI(title="oVirt SD")


def get_engine_connection():
    """Get connection from env"""
    conn = sdk.Connection(
        url=os.environ.get("OVIRT_URL"),
        username=os.environ.get("OVIRT_USERNAME"),
        password=os.environ.get("OVIRT_PASSWORD"),
        insecure=bool(os.environ.get("OVIRT_INSECURE")) | False,
        timeout=int(os.environ.get("OVIRT_SD_TIMEOUT")) | 60,
    )
    try:
        yield conn
    finally:
        conn.close()


@app.get("/hosts", response_model=list[dict])
async def get_hosts_targets(conn: sdk.Connection = Depends(get_engine_connection)):
    """Get hosts targets endpoint"""
    return HostsServiceDiscovery(conn).get_targets_group()


@app.get("/vms", response_model=list[dict])
async def get_vms_targets(conn: sdk.Connection = Depends(get_engine_connection)):
    """Get virtual machines targets endpoint"""
    return VMServiceDiscovery(conn).get_targets_group()


def main():
    """Main HTTP"""
    uvicorn.run(app, port=int(os.environ.get("OVIRT_SD_PORT")))


if __name__ == "__main__":
    main()
