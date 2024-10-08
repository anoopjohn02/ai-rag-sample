"""
Device service module
"""
import uuid
from typing import List

from app.data import DeviceRepo, Devices
from app.models.device import DeviceDto

repo = DeviceRepo()

def save_devices(devices:[DeviceDto]):
    """
    Method to save devices
    """
    for device in devices:
        entity = Devices()
        entity.id = uuid.uuid1()
        entity.name = device.name
        entity.description = device.description
        entity.type = device.type
        repo.save_device(entity)

def get_user_devices(user_id: uuid) -> List[DeviceDto]:
    """
    Method to get user devices
    """
    devices = repo.get_user_devices(user_id)
    return [DeviceDto(**device.__dict__) for device in devices]