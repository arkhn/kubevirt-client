# V1Disk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | [**V1BlockSize**](V1BlockSize.md) | If specified, the virtual disk will be presented with the given block sizes. | [optional] 
**boot_order** | **int** | BootOrder is an integer value &gt; 0, used to determine ordering of boot devices. Lower values take precedence. Each disk or interface that has a boot order must have a unique value. Disks without a boot order are not tried if a disk with a boot order exists. | [optional] 
**cache** | **str** | Cache specifies which kvm disk cache mode should be used. Supported values are: none: Guest I/O not cached on the host, but may be kept in a disk cache. writethrough: Guest I/O cached on the host but written through to the physical medium. Slowest but with most guarantees. writeback: Guest I/O cached on the host. Defaults to none if the storage supports O_DIRECT, otherwise writethrough. | [optional] 
**cdrom** | [**V1CDRomTarget**](V1CDRomTarget.md) | Attach a volume as a cdrom to the vmi. | [optional] 
**changed_block_tracking** | **bool** | ChangedBlockTracking indicates this disk should have CBT option Defaults to false. | [optional] 
**dedicated_io_thread** | **bool** | dedicatedIOThread indicates this disk should have an exclusive IO Thread. Enabling this implies useIOThreads &#x3D; true. Defaults to false. | [optional] 
**disk** | [**V1DiskTarget**](V1DiskTarget.md) | Attach a volume as a disk to the vmi. | [optional] 
**error_policy** | **str** | If specified, it can change the default error policy (stop) for the disk | [optional] 
**io** | **str** | IO specifies which QEMU disk IO mode should be used. Supported values are: native, default, threads. | [optional] 
**lun** | [**V1LunTarget**](V1LunTarget.md) | Attach a volume as a LUN to the vmi. | [optional] 
**name** | **str** | Name is the device name | [default to '']
**serial** | **str** | Serial provides the ability to specify a serial number for the disk device. | [optional] 
**shareable** | **bool** | If specified the disk is made sharable and multiple write from different VMs are permitted | [optional] 
**tag** | **str** | If specified, disk address and its tag will be provided to the guest via config drive metadata | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


