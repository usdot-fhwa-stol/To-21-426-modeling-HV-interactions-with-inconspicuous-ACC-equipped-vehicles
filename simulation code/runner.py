import os
import sys
import optparse
import random

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa
from generate_sumo_files import *
from generate_sumo_files import *
# sys.stdout = open('C:/Qinzheng/Projects/AMS car-following and lane changing/Use case/final ring road/configuration/print.txt', 'wt')
cfg_file_name = "./configuration/ring_road.sumocfg"
generate_cfg_file(cfg_file_name)
route_distri = "./configuration/ring_road.rou.xml"
detector_file = "./configuration/detector.add.xml"
edge_list=[]
route_id_list=['r1','r2','r3','r4']
initial_route_1=""
initial_route_2="E91 "
initial_route_3=""
initial_route_4=""

#define routes
def edges(start_id, end_id,current_route):
    for i in range(start_id, end_id):
        temp = "E" + str(i) + " "
        current_route+=temp
    current_route=current_route.rstrip()
    return current_route
route_1=edges(0,91,initial_route_1)
route_2=edges(16,91,initial_route_2)
route_3=edges(0,41,initial_route_3)
route_4=edges(16,41,initial_route_4)
route_3+=" E92"
route_4+=" E92"

edge_list.append(route_1)
edge_list.append(route_2)
edge_list.append(route_3)
edge_list.append(route_4)

detector_lane_list = []
detector_id_list = []
detector_pos_list = []
current_detector = 0

#define detector id and the location of the detector that will be located on each link
for edge_id in range(0, 91):
    if edge_id == 16 or edge_id == 40:
        detector_id_start = 1
        detector_id_end = 5
    else:
        if edge_id <= 62:
            detector_id_start = 0
            detector_id_end = 4
        else:
            detector_id_start = 0
            detector_id_end = 3
    if edge_id == 15:
        pos = 35
    elif edge_id == 41:
        pos = 24
    else:
        pos = 50
    for detector_id in range(detector_id_start, detector_id_end):
        lane_id = "E" + str(edge_id) + "_" + str(detector_id)
        detector_lane_list.append(lane_id)
        detector_id_list.append("e1_" + str(current_detector))
        detector_pos_list.append(pos)
        current_detector += 1

# detector_pos = 50.00
detector_out = "out.xml"
period = 30.00 #data collection period
HV_list=['HV','HV1','HV2','HV3','truck'] # vehicle type

#run simulation
def run(simulation_period):
    original_vehicle_type={}
    for step in range(simulation_period):
        id_list = traci.vehicle.getIDList() #get id of vehicles on the road network
        for current_veh_id in id_list:
            current_veh_type = traci.vehicle.getTypeID(current_veh_id)
            if current_veh_id not in original_vehicle_type.keys():
                original_vehicle_type[current_veh_id]=current_veh_type
            leader_veh_info=traci.vehicle.getLeader(current_veh_id)
            if leader_veh_info is not None:
                leader_veh_id,distance_to_leader=leader_veh_info
                leader_veh_type=traci.vehicle.getTypeID(leader_veh_id)
                if leader_veh_type=='ACC':
                    # Change the idm parameters of HV if it follows ADAS-equipped vehicle now and follows HV previously
                    if current_veh_type=='HV':
                        traci.vehicle.setType(current_veh_id,'Following-ACC')
                    if current_veh_type=='HV1':
                        traci.vehicle.setType(current_veh_id, 'Following-ACC1')
                    if current_veh_type=='HV2':
                        traci.vehicle.setType(current_veh_id, 'Following-ACC2')
                    if current_veh_type=='HV3':
                        traci.vehicle.setType(current_veh_id, 'Following-ACC3')
                    # print("changed_type:", traci.vehicle.getTypeID(current_veh_id))
                else:
                    # Change the idm parameters of HV if it follows ADAS-equipped vehicles previously and follows HV now
                    if current_veh_type in ['Following-ACC','Following-ACC1','Following-ACC2','Following-ACC3']:
                        ori_veh_type=original_vehicle_type[current_veh_id]
                        traci.vehicle.setType(current_veh_id, ori_veh_type)
        traci.simulationStep()
    traci.close()

#define args that will be used in the simulation and in the output
def genetrate_args(capacity_test,demand,MPR_ACC,trajectories,trip_info,fcd,prefix):
    gui = False
    warning = True
    seed = False
    seed_number=23491
    if gui:
        sumoBinary = checkBinary('sumo-gui')
        args = [sumoBinary, "-c", "./configuration/ring_road.sumocfg", "--quit-on-end"]
    else:
        sumoBinary = checkBinary('sumo')
        args = [sumoBinary, "-c", "./configuration/ring_road.sumocfg"]
    if warning:
        args.append("--no-warnings")
        args.append("true")
    if not capacity_test:
        case_description = "Demand-" + str(demand) + "-MPR_ACC-" + str(MPR_ACC) + "-"
        # case_description ='Seed-'+str(seed_number)+ "-Demand-" + str(demand) + "-MPR_ACC-" + str(MPR_ACC) + "-"

        if prefix:
            args.append("--output-prefix")
            # args.append("TIME")
            args.append(case_description)
        if seed:
            args.append("--seed")
            args.append(str(seed))
        if trajectories:
            args.append("--amitran-output")
            args.append("trajectories.xml")
        if trip_info:
            args.append("--tripinfo-output")
            args.append("tripinfo.xml")
        if fcd:
            args.append("--fcd-output")
            args.append("fcd.xml")
    return args
def simulation(capacity_test,starting_demand,ending_demand,demand_interval,starting_mpr,ending_mpr,mpr_interval,trajectories,trip_info,fcd,prefix,
               route1_ratio,route2_ratio,route3_ratio,route4_ratio,HV_ratio,HV1_ratio,HV2_ratio,HV3_ratio,truck_ratio):
    #test different traffic demand
    for demand in range(starting_demand,ending_demand,demand_interval):
        #test different market penetration rate
        for MPR_ACC in range(starting_mpr,ending_mpr,mpr_interval):
            MPR_ACC=MPR_ACC*0.01
            args = genetrate_args(capacity_test, demand, MPR_ACC,trajectories,trip_info,fcd,prefix)
            print("args:")
            print(args)
            # demand=4000
            # route1_ratio = 0.915
            # route2_ratio = 0.05
            # route3_ratio = 0.03
            # route4_ratio = 0.005
            # define volume of different routes
            route_1_demand = math.ceil(demand * route1_ratio)
            route_2_demand = math.ceil(demand * route2_ratio)
            route_3_demand = math.ceil(demand * route3_ratio)
            route_4_demand = math.ceil(demand * route4_ratio)
            # route_volume=[]
            total_demand = []
            total_demand.append(demand)

            # split the volume on main route into HV and ACC
            route_1_demand_HV = route_1_demand * (1 - MPR_ACC)
            route_1_demand_ACC = route_1_demand * MPR_ACC
            route_ACC_volume = [math.ceil(route_1_demand_ACC * route1_ratio),
                                math.ceil(route_1_demand_ACC * route2_ratio),
                                math.ceil(route_1_demand_ACC * route3_ratio),
                                math.ceil(route_1_demand_ACC * route4_ratio)]
            # define the vehicle type of HV along each route
            # HV_ratio = 0.7
            # HV1_ratio = 0.1
            # HV2_ratio = 0.1
            # HV3_ratio = 0.08
            # truck_ratio = 0.02
            route1_HV_type_volume = [math.ceil(route_1_demand_HV * HV_ratio), math.ceil(route_1_demand_HV * HV1_ratio),
                                     math.ceil(route_1_demand_HV * HV2_ratio), math.ceil(route_1_demand_HV * HV3_ratio),
                                     math.ceil(route_1_demand_HV * truck_ratio)]
            route2_type_volume = [math.ceil(route_2_demand * HV_ratio), math.ceil(route_2_demand * HV1_ratio),
                                  math.ceil(route_2_demand * HV2_ratio), math.ceil(route_2_demand * HV3_ratio),
                                  math.ceil(route_2_demand * truck_ratio)]
            route3_type_volume = [math.ceil(route_3_demand * HV_ratio), math.ceil(route_3_demand * HV1_ratio),
                                  math.ceil(route_3_demand * HV2_ratio), math.ceil(route_3_demand * HV3_ratio),
                                  math.ceil(route_3_demand * truck_ratio)]
            route4_type_volume = [math.ceil(route_4_demand * HV_ratio), math.ceil(route_4_demand * HV1_ratio),
                                  math.ceil(route_4_demand * HV2_ratio), math.ceil(route_4_demand * HV3_ratio),
                                  math.ceil(route_4_demand * truck_ratio)]
            route_volume = [route1_HV_type_volume, route2_type_volume, route3_type_volume, route4_type_volume]
            # print("route1_HV_type_volume:",route1_HV_type_volume)
            # print("route2_type_volume:", route2_type_volume)
            # print("route3_type_volume:", route3_type_volume)
            # print("route4_type_volume:", route4_type_volume)
            # print("route_ACC_volume:", route_ACC_volume)
            if capacity_test: #in the simulation capacity_test is always defined as False
                detector_out="det_capacity_output_volume" + str(total_demand[0]) + '.xml'
            else:
                detector_out = "nontest_capacity_detector" + '.xml'
            start_time=0
            if capacity_test:
                end_time = 600 + 3 * 3600
            else:
                end_time = 600 + 1 * 3600
            #generate routes of the road network
            generate_route_file(route_volume, route_ACC_volume, route_distri, MPR_ACC, start_time, end_time,
                                route_id_list, edge_list,
                                HV_list)
            # generate detectors of the road network
            generate_detector_file(detector_id_list, detector_lane_list, detector_pos_list, period, detector_out,
                                   detector_file)
            # generate sumocfg file
            generate_cfg_file(cfg_file_name)
            traci.start(args)

            run(end_time)

if __name__ == "__main__":
    # gui = True
    # warning=True
    # seed = False
    # trajectories = False
    # trip_info = False
    # fcd = False

    capacity_test = False
    trajectories = False
    trip_info = True
    fcd = False
    prefix=True
    starting_demand=2000
    ending_demand=2050
    demand_interval=50
    starting_mpr=0
    ending_mpr=100
    mpr_interval=10
    # 0.915 0.05
    route1_ratio = 0.915
    route2_ratio = 0.05
    route3_ratio = 0.03
    route4_ratio = 0.005
    HV_ratio = 0.7
    HV1_ratio = 0.1
    HV2_ratio = 0.1
    HV3_ratio = 0.08
    truck_ratio = 0.02
    simulation(capacity_test,starting_demand,ending_demand,demand_interval,starting_mpr,ending_mpr,mpr_interval,trajectories,trip_info,fcd,prefix,
               route1_ratio,route2_ratio,route3_ratio,route4_ratio,HV_ratio,HV1_ratio,HV2_ratio,HV3_ratio,truck_ratio)

