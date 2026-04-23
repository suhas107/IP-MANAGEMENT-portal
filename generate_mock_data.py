import csv
import random
from datetime import datetime, timedelta

def random_date(start_year=2015, end_year=2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d')

def generate_varieties():
    with open('mock_varieties.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Cat', 'Status', 'Year', 'Duration', 'PPVFR', 'Agency', 'Yield', 'Zones', 'States', 'Grain Types', 'Pests', 'Diseases', 'Abiotic Stress', 'Special Traits'])
        
        for i in range(1, 151):
            status = random.choice(['Filed', 'Granted', 'Licensed'])
            writer.writerow([
                f'IIRR-VAR-20{i:03d}',
                random.choice(['Variety', 'Hybrid']),
                status,
                random.randint(2015, 2024),
                random.randint(110, 150),
                random.choice(['Yes', 'No']),
                random.choice(['CVRC', 'SVRC', 'ICAR']),
                f'{round(random.uniform(4.0, 8.5), 1)} t/ha',
                random.choice(['Zone I, Zone II', 'Zone III', 'Zone II, Zone IV']),
                random.choice(['Telangana, AP', 'Punjab, Haryana', 'Odisha', 'West Bengal']),
                random.choice(['Medium Slender', 'Short Bold', 'Long Slender']),
                random.choice(['Brown Plant Hopper', 'Gall Midge', 'Stem Borer']),
                random.choice(['Blast', 'Bacterial Leaf Blight', 'Sheath Blight']),
                random.choice(['Salinity', 'Drought', 'Submergence', 'None']),
                random.choice(['High Zinc', 'High Protein', 'Aromatic', 'None'])
            ])

def generate_patents():
    with open('mock_patents.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Type', 'Title', 'Status', 'Filed', 'Expiry', 'Company', 'License / MoU Date', 'Office Action', 'Hearing', 'Fee', 'Fee Date', 'Royalty', 'Royalty Date'])
        
        types = ['PatentProduct'] * 110 + ['PatentProcess'] * 110 + ['PatentDesign'] * 110
        
        for i, p_type in enumerate(types, 1):
            status = random.choice(['Filed', 'Granted', 'Licensed'])
            is_licensed = status == 'Licensed'
            filed = random_date(2010, 2022)
            expiry = (datetime.strptime(filed, '%Y-%m-%d') + timedelta(days=20*365)).strftime('%Y-%m-%d')
            
            writer.writerow([
                f'IIRR-PAT-30{i:03d}',
                p_type,
                f'Automated Agritech Solution Mk {i}',
                status,
                filed,
                expiry,
                f'AgriCorp {i} Ltd' if is_licensed else '',
                random_date(2023, 2024) if is_licensed else '',
                random_date(2024, 2025) if status == 'Filed' else '',
                random_date(2024, 2025) if status == 'Filed' else '',
                round(random.uniform(50000, 500000), 2) if is_licensed else '',
                random_date(2023, 2024) if is_licensed else '',
                round(random.uniform(10000, 100000), 2) if is_licensed else '',
                random_date(2023, 2024) if is_licensed else ''
            ])

def generate_brands():
    with open('mock_brands.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Type', 'Name', 'Status', 'Company', 'License / MoU Date', 'Fee', 'Royalty', 'Royalty Date'])
        
        types = ['Copyright'] * 120 + ['Trademark'] * 60 + ['Logo'] * 60
        
        for i, b_type in enumerate(types, 1):
            status = random.choice(['Filed', 'Granted', 'Licensed'])
            is_licensed = status == 'Licensed'
            
            writer.writerow([
                f'IIRR-BRD-40{i:03d}',
                b_type,
                f'IIRR Official Asset V{i}',
                status,
                f'MediaCorp {i}' if is_licensed else '',
                random_date(2022, 2024) if is_licensed else '',
                round(random.uniform(5000, 50000), 2) if is_licensed else '',
                round(random.uniform(1000, 20000), 2) if is_licensed else '',
                random_date(2023, 2024) if is_licensed else ''
            ])

if __name__ == '__main__':
    generate_varieties()
    generate_patents()
    generate_brands()
    print("Mock data CSV files generated successfully.")