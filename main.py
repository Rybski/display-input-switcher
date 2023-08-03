import monitorcontrol    

monitor_list : list = monitorcontrol.get_monitors()
#print(monitor_list)

for monitor in monitor_list:
    with monitor as monitor_ctx:
        #print(monitor_ctx.get_vcp_capabilities()) 
        if(monitor_ctx.get_vcp_capabilities()["model"] == 'VG242Y P'):      # My monitor model
            #print(monitor_ctx.get_input_source())
            monitor_ctx.set_input_source(17)                                # DP1->15, HDMI1->17, HDMI2->18
            
