import os
from os.path import expanduser
import subprocess

home = expanduser("~")

# catkin_ws_path = home + '/workspace/catkin_ws'
catkin_ws_path = home + '/workspace/Context-POMDP'

summit_path = home + "/summit"

conda_path = home+"/miniconda3"

if not os.path.isdir(catkin_ws_path):
    catkin_ws_path = home + '/whatmatters'

result_path = home + '/whatmatters/driving_data'


# check whether the folders exist:
if not os.path.isdir(result_path):
    os.makedirs(result_path)
    print("Made result folder " + result_path)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--image',
                        type=str,
                        default="cppmayo/melodic_cuda10_1_cudnn7_libtorch_opencv4_ws",
                        help='Image to launch')
    parser.add_argument('--port',
                        type=int,
                        default=2000,
                        help='summit_port')
    parser.add_argument('--gpu',
                        type=int,
                        default=0,
                        help='GPU to use')
    parser.add_argument('--recordbag',
                        type=int,
                        default=0,
                        help='record ros bags')
    parser.add_argument('--mode',
                        type=str,
                        default='joint_pomdp',
                        help='driving mode') 


    config = parser.parse_args()

    # I add conda_path so as to use conda environment from host machine inside docker
    additional_mounts = "-v " + catkin_ws_path + ":/root/catkin_ws -v " + summit_path + ":/root/summit " + \
        "-v " + conda_path + ":/home/tbaphong/miniconda3 " + "-v /home/tbaphong/.ros:/root/.ros "

    cmd_args = "docker run --rm --runtime=nvidia -it --network host " + \
                "-v " + result_path + ":/root/driving_data " + \
                                additional_mounts + \
                "-e DISPLAY=${DISPLAY} -v /tmp/.X11-unix:/tmp/.X11-unix " + \
                config.image + " " + str(config.gpu) + " " + str(config.port) \
                + " " + str(config.recordbag) + " " + str(config.mode)

    print(cmd_args)
    subprocess.call(cmd_args.split())
