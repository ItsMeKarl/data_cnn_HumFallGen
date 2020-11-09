import imageio
import os.path
import os

for current_dir, dirs, files in os.walk("."):
    for name_dirs in dirs:
        if name_dirs == "2_line_hit_ROU":
            last_path = os.getcwd()
            print(last_path)
            os.chdir(name_dirs)
            print(os.getcwd())
            for current_dir_2, dirs_2, files_2 in os.walk("."):
                for name_files in files_2:

                    name_r = name_files[:-4]
                    print(name_r)
                    print(last_path)
                    im = imageio.imread(name_r +'.HDR')
                    imageio.imwrite( name_r + '.png', im[:, :, 0])
                    # удаление HDR, чтоб не мешались
                    os.remove(name_r +'.HDR') 


