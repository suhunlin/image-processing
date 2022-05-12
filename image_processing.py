from PIL import Image
import os
def is_image_file_by_filename(filename):
    result = False
    if filename.endswith('.jpeg') or filename.endswith('.png'):
        result = True
    return result

def get_filename_list_from_path(path):
    filename_list = []
    if os.path.exists(path):
        for filename in os.listdir(path): #(os.listdir(path))根據傳入的path找到資料夾，並回傳資料夾內所有檔案的filename
            if is_image_file_by_filename(filename):
                filename_list.append(filename)
    else:
        print('請傳入正確的檔案路徑 !!!')
    return filename_list

def conver_image_to_gray(path,filename_list):
    result = False
    if not filename_list:
        print('無檔案名稱!!!')
    else:
        for filename in filename_list:
            full_path = os.path.join(path,filename)
            new_filename = 'gray_' + filename
            new_full_path = os.path.join(path,new_filename)
            if os.path.exists(full_path):
                try:
                    image_file = Image.open(full_path)
                    image_file = image_file.convert('L')
                    image_file.save(new_full_path)
                    result = True
                except Exception as error_message:
                    print(error_message)
            else:
                print('找無影像檔!!!無法將影像轉成灰階!!!')
    return result

def resize_image_by_width(path,filename_list,width):
    result = False
    if not filename_list:
        print('無檔案名稱!!!')
    else:
        for filename in filename_list:
            full_path = os.path.join(path,filename)
            if os.path.exists(full_path):
                try:
                    image_file = Image.open(full_path)
                    ratio = float(width / image_file.size[0]) #先根據傳入的width，算出width實際放大或縮小幾倍
                    height = int(image_file.size[1] * ratio) #把原始圖檔的height乘以上一行算出的倍率ratio
                    resize_image = image_file.resize((width,height))
                    new_filename = str(width) + 'x' + str(height) + '_' + filename
                    new_full_path = os.path.join(path,new_filename)
                    resize_image.save(new_full_path)
                    result = True
                except Exception as error_message:
                    print(error_message)
            else:
                print('找無影像檔!!!無法將影像根據width比例resize!!!')
    return result

def resize_image_by_height(path,filename_list,height):
    result = False
    if not filename_list:
        print('無檔案名稱!!!')
    else:
        for filename in filename_list:
            full_path = os.path.join(path,filename)
            if os.path.exists(full_path):
                try:
                    image_file = Image.open(full_path)
                    ratio = float(height / image_file.size[1])#先根據傳入的height，算出width實際放大或縮小幾倍
                    width = int(image_file.size[0] * ratio)#把原始圖檔的height乘以上一行算出的倍率ratio
                    resize_image = image_file.resize((width,height))
                    new_filename = str(width) + 'x' + str(height) + '_' + filename
                    new_full_path = os.path.join(path, new_filename)
                    resize_image.save(new_full_path)
                    result = True
                except Exception as error_message:
                    print(error_message)
            else:
                print('找無影像檔!!!無法將影像根據height比例resize!!!')
    return result

def main():
    path = '/Users/shu-hunglin/Desktop/pic'
    width = 100
    height = 200
    filename_list = get_filename_list_from_path(path)
    # if(conver_image_to_gray(path,filename_list)):
    #     print('檔案轉成灰階完成!!!')
    # else:
    #     print('檔案轉成灰階失敗!!!')
    # if(resize_image_by_width(path,filename_list,width)):
    #     print('根據with比率來resize圖檔成功!!!')
    # else:
    #     print('根據with比率來resize圖檔失敗!!!')
    if(resize_image_by_height(path,filename_list,height)):
        print('根據height比率來resize圖檔成功!!!')
    else:
        print('根據height比率來resize圖檔失敗!!!')

if __name__ == '__main__':
    main()
