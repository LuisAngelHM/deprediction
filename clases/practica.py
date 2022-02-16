class Ropa:
    def __init__(self, marca, precio, color) -> None:
        self.marca = marca
        self.precio = precio
        self.color = color
    
    def descripcion(self):
        return 'blusa de marca {} de color {} tiene un precio de {}'.format(self.marca, self.color, self.precio)

    def __str__(self) -> str:
        return f"Blusa de marca {self.marca} con precio de {self.precio}"
    
    def __getattribute__(self, __name: str) -> Any:
        pass

def main():
    blusa = Ropa("Adiddas", 50, "Negro")
    print(f"la ropa es {blusa}")    

if __name__ == "__main__":
   
    main()

