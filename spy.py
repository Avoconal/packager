import wmi
core = wmi.WMI()
if input('输入0查看缩略信息,输入1查看完整信息:') == '0':
    # if True:
    # ComputerSystem
    temp = core.Win32_ComputerSystem()[0]
    print('设备制造商：{}\n设备型号：{}\n设备代号：{}\n设备名称：{}\n'.format(
        temp.Manufacturer, temp.Model, temp.ChassisSKUNumber, temp.Name))
    # BIOS
    temp = core.Win32_BIOS()[0]
    print('主板序列号：{}\nBIOS版本：{}\n'.format(
        temp.SerialNumber, temp.SMBIOSBIOSVersion))
    # OperatingSystem
    temp = core.Win32_OperatingSystem()[0]
    print('系统名称：{}\n系统版本：{}\n系统位数：{}\n系统序列号：{}\n'.format(
        temp.Caption, temp.BuildNumber, temp.OSArchitecture, temp.SerialNumber))
    # Processor
    temp = core.Win32_Processor()[0]
    print('CPU名称：{}\nCPU核心数：{}\nCPU线程数：{}\n'.format(
        temp.Name, temp.NumberOfEnabledCore, temp.NumberOfLogicalProcessors))
    # VideoController
    for i in range(len(core.Win32_VideoController())):
        temp = core.Win32_VideoController()[i]
        print('GPU {} 信息：\n名称：{}\n制造商：{}\n模式信息：{}\n最大刷新率：{} Hz\n'.format(i,  temp.Name,
                                                                         temp.AdapterCompatibility, temp.VideoModeDescription, temp.MaxRefreshRate))
    # PhysicalMemory
    for i in range(len(core.Win32_PhysicalMemory())):
        temp = core.Win32_PhysicalMemory()[i]
        print('内存 {} 信息：\n制造商：{}\n速度：{} MHz\n容量：{} GB\n'.format(i,  temp.Manufacturer,
                                                                temp.Speed, int(temp.Capacity)/1024**3))
    # DiskDrive
    for i in range(len(core.Win32_DiskDrive())):
        temp = core.Win32_DiskDrive()[i]
        print('磁盘 {} 信息：\n型号：{}\n序列号：{}\n容量：{} GB\n'.format(i,  temp.Model,
                                                            temp.SerialNumber, int(temp.Size)/1024**3))
    # NetworkAdapter
    for i in range(len(core.Win32_NetworkAdapter())):
        temp=core.Win32_NetworkAdapter()[i]
        print('网络适配器 {} 信息：\n名称：{}\n制造商：{}\nMAC地址：{}\n'.format(
            i, temp.Name, temp.Manufacturer, temp.MACAddress))
else:
    print(core.Win32_ComputerSystem()[0])
    print(core.Win32_BIOS()[0])
    print(core.Win32_OperatingSystem()[0])
    print(core.Win32_Processor()[0])
    print(''.join([str(i) for i in core.Win32_VideoController()]))
    print(''.join([str(i) for i in core.Win32_PhysicalMemory()]))
    print(''.join([str(i) for i in core.Win32_DiskDrive()]))
    print(''.join([str(i) for i in core.Win32_NetworkAdapter()]))
input('输入任意内容退出：')
