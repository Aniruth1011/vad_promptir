import os 
import cv2 
from tqdm import tqdm 

videos = r"/mnt/d/ssmctb/frames"
save_base_dir = r"/mnt/d/PromptIR/data/Train/vad"

save_input = os.path.join(save_base_dir , 'input')
save_output = os.path.join(save_base_dir , 'target')

writer = open(r"data_dir/vad/vad.txt" , "w")
video_num = 0

for each_video in tqdm(os.listdir(videos)):

    video_num+=1
    video_path = os.path.join(videos , each_video)

    for each_frame in os.listdir(video_path):

        frame_path = os.path.join(videos , each_video , each_frame)

        frame = cv2.imread(frame_path)

        save_file_name = str(video_num) + '_' + str(each_frame)

        save_input_path = os.path.join(save_input ,  save_file_name)
        save_target_path = os.path.join(save_output ,  save_file_name)

        cv2.imwrite(save_input_path , frame)
        cv2.imwrite(save_target_path , frame)

        writer.write(save_file_name)
        writer.write("\n")

