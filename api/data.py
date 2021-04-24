class Data:
    @staticmethod
    def addImage(imageName):
        with open(imageName, 'rb') as f:
            image = f.read()
        
        return image

    items = [
        {
            "__id": 1,
            "name": "Biscuit",
            # "images": [
            #     addImage.__func__('assets/biscuit-1.jpeg'),
            #     addImage.__func__('assets/biscuit-2.jpg')
            # ],
            "price": 9.99,
            "itemsLeft": 3
        },
        {
            "__id": 2,
            "name": "Cookie",
            # "images": [
            #     addImage.__func__('assets/cookie-1.jpeg'),
            #     addImage.__func__('assets/cookie-2.jpg')
            # ],
            "price": 7.00,
            "itemsLeft": 5
        },
        {
            "__id": 3,
            "name": "Coke",
            # "images": [
            #     addImage.__func__('assets/coke-1.jpg'),
            #     addImage.__func__('assets/coke-2.jpg')
            # ],
            "price": 2.79,
            "itemsLeft": 1
        },
        {
            "__id": 4,
            "name": "Chips",
            # "images": [
            #     addImage.__func__('assets/chips-1.jpg'),
            #     addImage.__func__('assets/chips-2.jpg')
            # ],
            "price": 5.45,
            "itemsLeft": 9
        }
    ]