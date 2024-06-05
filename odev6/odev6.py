import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Rastgele Koordinatları Üretmek ve Excel'e Kaydetmek
def generate_and_save_coordinates(num_points=1000, filename='coordinates.xlsx'):
    x_coords = np.random.randint(0, 1001, num_points)
    y_coords = np.random.randint(0, 1001, num_points)
    df = pd.DataFrame({'X': x_coords, 'Y': y_coords})
    df.to_excel(filename, index=False)
    print(f'Koordinatlar {filename} dosyasına kaydedildi.')

# 2. Excel Dosyasından Koordinatları Okumak ve Görselleştirmek
def read_and_plot_coordinates(filename='coordinates.xlsx'):
    df = pd.read_excel(filename)
    x_coords = df['X']
    y_coords = df['Y']
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Koordinatları')
    plt.ylabel('Y Koordinatları')
    plt.title('Rastgele Noktalar')
    plt.show()

# 3. Noktaları Izgaraya Bölmek ve Farklı Renklerle Görselleştirmek
def plot_colored_grid(filename='coordinates.xlsx', grid_size=200):
    df = pd.read_excel(filename)
    x_coords = df['X']
    y_coords = df['Y']

    # Renk paleti oluşturma
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'brown', 'cyan', 'magenta']
    color_dict = {}

    plt.figure(figsize=(10, 10))
    for i in range(0, 1000, grid_size):
        for j in range(0, 1000, grid_size):
            grid_points = df[(x_coords >= i) & (x_coords < i + grid_size) & 
                             (y_coords >= j) & (y_coords < j + grid_size)]
            if not grid_points.empty:
                # Her grid hücresi için renk seçimi
                color_key = (i // grid_size, j // grid_size)
                if color_key not in color_dict:
                    color_dict[color_key] = colors[len(color_dict) % len(colors)]
                plt.scatter(grid_points['X'], grid_points['Y'], color=color_dict[color_key], alpha=0.5)

    plt.xlabel('X Koordinatları')
    plt.ylabel('Y Koordinatları')
    plt.title(f'{grid_size}x{grid_size} Izgaraya Bölünmüş Rastgele Noktalar')
    plt.grid(True)
    plt.show()

# Ana fonksiyon
def main():
    filename = 'coordinates.xlsx'
    
    # Rastgele koordinatları üret ve kaydet
    generate_and_save_coordinates(filename=filename)
    
    # Koordinatları oku ve plot et
    read_and_plot_coordinates(filename=filename)
    
    # 200x200 grid ile görselleştirme
    grid_size = 200
    plot_colored_grid(filename=filename, grid_size=grid_size)

# Programı çalıştır
if __name__ == "__main__":
    main()