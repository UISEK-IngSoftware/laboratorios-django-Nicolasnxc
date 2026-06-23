#include <iostream>
#include <string> 

using namespace std;

// ==========================================
// PASO 1: EL MOLDE (EL NODO)
// ==========================================
struct PaginaWeb {
    string direccionUrl;       // El "dato"
    PaginaWeb* paginaAnterior; // El puntero al nodo "siguiente" (hacia abajo)
};


// ==========================================
// PASO 2: EL ADMINISTRADOR (LA CLASE/PILA)
// ==========================================
class HistorialNavegacion {
private:
    PaginaWeb* paginaActual; // El puntero "top" (cima)

public:
    // CONSTRUCTOR: Al nacer el historial (abrir la pestaña),
    // la pantalla está en blanco, por eso apunta a la nada (nullptr).
    HistorialNavegacion() {
        paginaActual = nullptr;
    }

    // Destructor
    ~HistorialNavegacion() {
        while (!estaVacio()) {
            botonAtras(); 
        }
    }

    // ==========================================
    // /// >>> AQUÍ ESTÁ EL isEmpty <<<
    // ==========================================
    // Verifica si la pila no tiene elementos.
    bool estaVacio() {
        return paginaActual == nullptr;
    }

    // ==========================================
    // /// >>> AQUÍ ESTÁ EL PUSH <<<
    // ==========================================
    // Inserta un elemento en la cima de la pila.
    void visitarPagina(string nuevaUrl) {
        // Paso A: Compra una caja nueva en la memoria RAM
        PaginaWeb* nuevaPagina = new PaginaWeb();
        
        // Paso B: Le escribe el nombre de la URL adentro
        nuevaPagina->direccionUrl = nuevaUrl;

        // Paso C: Conecta el nodo nuevo con el que antes era el "top"
        nuevaPagina->paginaAnterior = paginaActual;

        // Paso D: El "top" ahora pasa a ser el nuevo nodo
        paginaActual = nuevaPagina;

        cout << "-> Has visitado: " << nuevaUrl << "\n";
    }

    // ==========================================
    // /// >>> AQUÍ ESTÁ EL POP <<<
    // ==========================================
    // Elimina el elemento que está en la cima de la pila.
    void botonAtras() {
        // Validación basada en isEmpty
        if (estaVacio()) {
            cout << "No hay páginas atrás en el historial.\n";
            return;
        }

        // Paso A: Guarda el nodo de la cima en un "respaldo" temporal
        PaginaWeb* paginaABorrar = paginaActual;

        cout << "<- Volviendo atrás desde: " << paginaActual->direccionUrl << "\n";

        // Paso B: Mueve el "top" al nodo de abajo
        paginaActual = paginaActual->paginaAnterior;

        // Paso C: Destruye el nodo eliminado de la memoria RAM
        delete paginaABorrar;
    }

    // ==========================================
    // /// >>> AQUÍ ESTÁ EL PEEK <<<
    // ==========================================
    // Muestra el valor en la cima (top) sin eliminarlo de la pila.
    string verPaginaActual() {
        if (estaVacio()) {
            return "Pestaña en blanco (Sin URL)";
        }
        return paginaActual->direccionUrl;
    }

    // ==========================================
    // /// >>> AQUÍ ESTÁ EL MÈTODO MOSTRAR <<<
    // ==========================================
    // Recorre toda la pila desde la cima hasta la base.
    void mostrarHistorial() {
        if (estaVacio()) {
            cout << "[El historial está vacío]\n";
            return;
        }

        // Nodo auxiliar para no perder el puntero "top" real
        PaginaWeb* auxiliar = paginaActual; 
        
        cout << "\n--- HISTORIAL DE LA PESTAÑA (Cima -> Base) ---\n";
        
        // Bucle que recorre los nodos hasta llegar al final (nullptr)
        while (auxiliar != nullptr) {
            cout << "   [ " << auxiliar->direccionUrl << " ]\n";
            auxiliar = auxiliar->paginaAnterior; // Avanza al nodo de abajo
        }
        cout << "-----------------------------------------------------------------\n\n";
    }
};

// ==========================================
// PASO 3: EL MUNDO REAL (PRUEBAS)
// ==========================================
int main() {
    HistorialNavegacion pestañaChrome;

    // Pruebas de PUSH
    pestañaChrome.visitarPagina("google.com");
    pestañaChrome.visitarPagina("youtube.com");
    pestañaChrome.visitarPagina("wikipedia.org");

    // Prueba de MOSTRAR
    pestañaChrome.mostrarHistorial();

    // Prueba de PEEK
    cout << "PEEK (Lo que está en la cima): " << pestañaChrome.verPaginaActual() << "\n\n";

    // Prueba de POP
    pestañaChrome.botonAtras();
    
    // Volvemos a MOSTRAR para ver los cambios
    pestañaChrome.mostrarHistorial();

    return 0;
}