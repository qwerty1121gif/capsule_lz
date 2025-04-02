import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

class BigMacStats:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        self.preprocess_data()
    
    def preprocess_data(self):
        # Вычисляем средние цены
        self.avg_prices = self.df.groupby('name')['dollar_price'].mean().reset_index()
        
        # Приводим названия стран к единому формату
        country_mapping = {
            'United States': 'United States of America',
            'Czech Republic': 'Czechia',
            'South Korea': 'South Korea',
            # Добавьте другие несовпадающие названия при необходимости
        }
        
        self.avg_prices['name'] = self.avg_prices['name'].replace(country_mapping)
        
        # Объединяем с геоданными
        self.world = self.world.merge(
            self.avg_prices,
            left_on='name',
            right_on='name',
            how='left'
        )
    
    def show_world_map(self):
        fig, ax = plt.subplots(figsize=(20, 10))
        self.world.plot(
            column='dollar_price',
            ax=ax,
            legend=True,
            legend_kwds={'label': "Средняя цена в долларах"},
            missing_kwds={'color': 'lightgrey'},
            cmap='OrRd'
        )
        
        plt.title('Средняя стоимость Биг Мака в мире')
        plt.axis('off')
        plt.show()
    
    def show_histogram(self):
        plt.figure(figsize=(15, 8))
        data = self.avg_prices.sort_values('dollar_price', ascending=False)
        
        bars = plt.bar(data['name'], data['dollar_price'])
        plt.xticks(rotation=90)
        plt.ylabel('Средняя цена в долларах')
        plt.title('Средняя стоимость Биг Мака по странам за все годы')
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height, 
                     f'{height:.2f}', ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()

# Файл main.py
from bigmac_stats import BigMacStats

def main():
    try:
        analyzer = BigMacStats('BigmacPrice.csv')
        analyzer.show_world_map()
        analyzer.show_histogram()
    
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        print("Убедитесь, что установлены все зависимости:")
        print("pip install geopandas matplotlib pandas")

if __name__ == "__main__":
    main()