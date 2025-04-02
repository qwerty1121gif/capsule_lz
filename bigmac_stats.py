import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

class BigMacStats:
    def __init__(self, file_path, shapefile_path):
        self.df = pd.read_csv(file_path)
        self.world = gpd.read_file(shapefile_path)
        self.preprocess_data()
    
    def preprocess_data(self):
        # Вычисляем средние цены
        self.avg_prices = self.df.groupby('name')['dollar_price'].mean().reset_index()
        
        # Сопоставление названий стран
        country_mapping = {
            'United States': 'United States of America',
            'Czech Republic': 'Czechia',
            'South Korea': 'Republic of Korea',
            'Russia': 'Russian Federation',
            'Taiwan': 'Taiwan',
            'Venezuela': 'Venezuela (Bolivarian Republic of)',
            'Tanzania': 'United Republic of Tanzania',
            'Syria': 'Syrian Arab Republic',
            'Iran': 'Iran (Islamic Republic of)',
            'Moldova': 'Republic of Moldova'
        }
        
        self.avg_prices['name'] = self.avg_prices['name'].replace(country_mapping)
        
        # Объединяем данные
        self.world = self.world.merge(
            self.avg_prices,
            left_on='SOVEREIGNT',  # Используем стандартное название страны в shapefile
            right_on='name',
            how='left'
        )
    
    def show_world_map(self):
        fig, ax = plt.subplots(figsize=(25, 15))
        self.world.plot(
            column='dollar_price',
            ax=ax,
            legend=True,
            legend_kwds={'label': "Средняя цена в долларах", 'orientation': "horizontal"},
            missing_kwds={'color': 'lightgrey'},
            cmap='OrRd',
            edgecolor='black',
            linewidth=0.3
        )
        
        plt.title('Средняя стоимость Биг Мака в мире', fontsize=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def show_histogram(self):
        plt.figure(figsize=(18, 10))
        data = self.avg_prices.sort_values('dollar_price', ascending=False)
        
        bars = plt.bar(data['name'], data['dollar_price'], color='#ff7f0e')
        plt.xticks(rotation=90, fontsize=10)
        plt.yticks(fontsize=12)
        plt.ylabel('Средняя цена в долларах', fontsize=14)
        plt.title('Средняя стоимость Биг Мака по странам за все годы', fontsize=16)
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, height, 
                     f'{height:.2f}', ha='center', va='bottom', fontsize=8)
        
        plt.tight_layout()
        plt.show()

