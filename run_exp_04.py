from dino_experiments.exp_04_dim_reduction import main as experiment_4
if __name__ == '__main__':
    experiment_4("fayoum", subfolder="fayoum/")
    experiment_4("fayoum", subfolder="fayoum_oriented/", norm_orient=False)