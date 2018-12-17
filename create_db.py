from src.infra.database import meta_data
from src.delivery.models import PDV

if __name__ == '__main__':
    meta_data.create_all()
