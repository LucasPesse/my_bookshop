def init_books_route(app):
    @app.get("/books")
    def get_books():
        return {
            "books": [
                {
                    "id": "aOEaEAAAQBAJ",
                    "title": 'Gatsby le Magnifique',
                    "author": 'F. Scott Fitzgerald',
                    "cover": 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fd28hgpri8am2if.cloudfront.net%2Fbook_images%2Fonix%2Fcvr9781471173936%2Fthe-great-gatsby-9781471173936_hr.jpg&f=1&nofb=1&ipt=c3d70780986667ca9254713e476aad55cdf9278bbec938b63e35588e1b39135d&ipo=images',
                    "price": '10.99'
                },
                {
                    "id": "-n4gCgAAQBAJ",
                    "title": "Ne tirez pas sur l'oiseau moqueur",
                    "author": 'Harper Lee',
                    "cover": 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F71VfG2K6J9L._SL1500_.jpg&f=1&nofb=1&ipt=d7355e89c3095f40fad3bf695a142c09995dd0f10c13d1b10cc3e2f49cd560ce&ipo=images',
                    "price": '12.99'
                },
                {
                    "id": "BFZlEAAAQBAJ",
                    "title": '1984',
                    "author": 'George Orwell',
                    "cover": 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2F2.bp.blogspot.com%2F-trdPWkJ6A6A%2FUgufOCfNDDI%2FAAAAAAAABeE%2Fp-h81IEmleQ%2Fs1600%2F1984_1.jpg&f=1&nofb=1&ipt=443e02a507bd1cac8dbd13deea3be59349e0215665edce63f1a1d1842ebed959&ipo=images',
                    "price": '14.99'
                },
                {
                    "id": "Ox5zwsnOp8MC",
                    "title": 'Orgueil et Préjugés',
                    "author": 'Jane Austen',
                    "cover": 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fproducts-images.di-static.com%2Fimage%2Fjane-austen-orgueil-et-prejuges%2F9782368860786-475x500-1.jpg&f=1&nofb=1&ipt=45216376fad3ac58b86c12385171e29e54d4643d345d923d52dc4fdcde6cec32&ipo=images',
                    "price": '9.99'
                }
            ]
        }
