import os
import time


def get_timestamp():
    formatted_time = time.strftime('%d-%b-%y||%H:%M:%S')
    return formatted_time


def get_project_root():
    return os.path.abspath('../')


def get_pytorch_root():
    return os.path.join(get_project_root(), 'pytorch')


def get_log_root():
    return os.path.join(get_pytorch_root(), 'log')


def get_data_root():
    return os.path.join(get_pytorch_root())


def get_image_root():
    return os.path.join(get_project_root(), 'img')


def get_checkpoint_root():
    return os.path.join(get_pytorch_root(), 'checkpoints')


def get_output_root():
    return os.path.join(get_pytorch_root(), 'out')


def main():
    print(get_log_root())


if __name__ == '__main__':
    main()
