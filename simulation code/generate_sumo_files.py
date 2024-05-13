import math
def generate_cfg_file(filename):
    # generate configuration file for SUMO
    with open(filename, "w", encoding="utf-8") as cfg:
        print(
            u"""<?xml version="1.0" encoding="UTF-8"?>

<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/sumoConfiguration.xsd">

    <input>
        <net-file value="ring_road.net.xml"/>
        <route-files value="ring_road.rou.xml"/>
        <additional-files value="detector.add.xml "/>
    </input>
    <report>
        <verbose value="true"/>
        <log value="log.txt"/>
        <duration-log.statistics value="true"/>
        <no-step-log value="true"/>
    </report>
    <random_number>
        <seed value="23423"/> 
    </random_number>
</configuration>
    """,file=cfg,)

# generate_cfg_file()
def generate_route_file(volume_list,route_ACC_volume,
    route_file_name,
    MPR_ACC,
    start_time,
    end_time,
    route_list,
    edge_list,
    HV_list):

    MPR_HV=1-MPR_ACC
    print("volume_list:",volume_list)
    print("route_list:", route_list)
    print("edge_list:", edge_list)
    with open(route_file_name, "w", encoding="utf-8") as file:
        print(
            u"""<?xml version="1.0" encoding="UTF-8"?>
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/routes_file.xsd">"""
            ,file=file)
        print(
            u"""
           <vType id="ACC" color="0,255,255" length="5"  maxSpeed="33.33"  carFollowModel="IDM" tau="0.6" minGap="2" accel="1.4" decel="2" lcStrategic="0.1" lcKeepRight="0"/>
            """, file=file
        )

        print(
            u"""
           <vType id="Following-ACC" color="0,255,255" length="5"  maxSpeed="33.28"  carFollowModel="IDM" tau="1.54" minGap="1.32" accel="0.73" decel="1.67" lcStrategic="0.1" lcKeepRight="0" lcAssertive="5"/>
            """, file=file
        )

        print(
            u"""
           <vType id="Following-ACC1" color="0,255,255" length="5"  maxSpeed="28.3"  carFollowModel="IDM" tau="1.54" minGap="1.32" accel="0.73" decel="1.67" lcStrategic="0.1" lcKeepRight="0" lcAssertive="5"/>
            """, file=file
        )

        print(
            u"""
           <vType id="Following-ACC2" color="0,255,255" length="5"  maxSpeed="25.3"  carFollowModel="IDM" tau="1.54" minGap="1.32" accel="0.73" decel="1.67" lcStrategic="0.1" lcKeepRight="0" lcAssertive="5"/>
            """, file=file
        )
        print(
            u"""
           <vType id="Following-ACC3" color="0,255,255" length="5"  maxSpeed="22.4"  carFollowModel="IDM" tau="1.54" minGap="1.32" accel="0.73" decel="1.67" lcStrategic="0.1" lcKeepRight="0" lcAssertive="5"/>
            """, file=file
        )
        # print("*********************************")
        print(
            u"""
            <vType id="HV" color="0,0,255" length="5" carFollowModel="IDM" maxSpeed="33.3" tau="1.6"  minGap="2" 
            accel="0.73" decel="1.67" speedFactor="1" stepping="0.25" lcStrategic="0.1" lcCooperative="1" lcAssertive="5" 
            lcSpeedGain="1" lcSpeedGainLookahead="0" lcLookaheadLeft="1" lcKeepRight="0" speedDev="0.1" />
            """, file=file
        )

        print(
            u"""
            <vType id="HV1" color="0,100,255" length="5" carFollowModel="IDM" maxSpeed="28.3" tau="1.6"  minGap="2" 
            accel="0.73" decel="1.67" speedFactor="1" stepping="0.25" lcStrategic="0.1" lcCooperative="1" lcAssertive="5" 
            lcSpeedGain="1" lcSpeedGainLookahead="0" lcLookaheadLeft="1" lcKeepRight="0" speedDev="0.1" />
            """, file=file
        )

        print(
            u"""
            <vType id="HV2" color="100,0,255" length="5" carFollowModel="IDM" maxSpeed="25.3" tau="1.6"  minGap="2" 
            accel="0.73" decel="1.67" speedFactor="1" stepping="0.25" lcStrategic="0.1" lcCooperative="1" lcAssertive="5" 
            lcSpeedGain="1" lcSpeedGainLookahead="0" lcLookaheadLeft="1" lcKeepRight="0" speedDev="0.1" />
            """, file=file
        )

        print(
            u"""
            <vType id="HV3" color="100,100,255" length="5" carFollowModel="IDM" maxSpeed="22.3" tau="1.6"  minGap="2" 
            accel="0.73" decel="1.67" speedFactor="1" stepping="0.25" lcStrategic="0.1" lcCooperative="1" lcAssertive="5" 
            lcSpeedGain="1" lcSpeedGainLookahead="0" lcLookaheadLeft="1" lcKeepRight="0" speedDev="0.1" />
            """, file=file
        )

        print(
            u"""
            <vType id="truck" color="125,50,255" length="15" carFollowModel="IDM" maxSpeed="20" tau="1.8"  minGap="2.5" 
            accel="0.70" decel="1.47" speedFactor="1" stepping="0.25" lcStrategic="0.8" lcCooperative="1" lcAssertive="1" 
            lcSpeedGain="999" lcSpeedGainLookahead="0" lcLookaheadLeft="10" lcKeepRight="0" speedDev="0.2" />
            """, file=file
        )

        flow_i = 1
        for route_i in range(len(volume_list)):
            # print("route_i:",route_i)
            route_id=route_list[route_i]
            type_volume=volume_list[route_i]
            edge=edge_list[route_i]
            # if route_i==0:
            #     volume_truck=math.ceil(type_volume*0.015)
            # else:
            #     volume_truck = math.ceil(type_volume * 0.03)


            print(u"""
        <route id="%s" edges="%s"/>"""%(route_id,edge),file=file,
            )
            if MPR_ACC>0:
                print(
                    u"""
                    <flow id="flow%d"  begin="%d" end= "%d" vehsPerHour="%f" type="ACC" route="%s" departLane="random" departSpeed="last" departPos="last"></flow>
                    """% (flow_i, start_time,end_time,route_ACC_volume[route_i],route_id),file=file
                )
                flow_i+=1
            if MPR_HV>0:
                for type_i in range(len(type_volume)):
                    volume=type_volume[type_i]
                    veh_type=HV_list[type_i]
                    print(
                        """
                       <flow id="flow%d"  begin="%d" end= "%d" vehsPerHour="%f" type="%s" route="%s" departLane="random" departSpeed="last" departPos="last" ></flow>
                        """ %(flow_i,start_time,end_time,volume,veh_type,route_id),file=file
                    )
                    flow_i += 1
        print(
            u"""
</routes>
            """, file=file)
def generate_detector_file(
        id_list,lane_list, pos, period,out_name,
        detector_additional_file="./configuration/detector.add.xml",
):
    with open(detector_additional_file, "w", encoding="utf-8") as file:
        print(
            u"""<?xml version="1.0" encoding="UTF-8"?>
<additional xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/additional_file.xsd">
<!-- Detectors -->
            """,file=file
        )
        for i in range(len(id_list)):
            print("""
            <inductionLoop id="%s" lane="%s" pos="%f" period="%f" file="%s"/>
            """%(id_list[i],lane_list[i],pos[i],period,out_name),file=file)
        print(u"""
</additional>
        """,file=file)





