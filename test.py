#include <iostream>
#include <cstdlib> // Для функций rand() и srand()
#include <ctime>   // Для функции time()

int main() {
    // Инициализируем генератор случайных чисел на основе текущего времени.
    // Это гарантирует разные числа при каждом запуске программы.
    srand(time(0)); 

    // Генерируем и выводим несколько случайных чисел.

    // Случайное число в диапазоне [0, RAND_MAX]
    int random_number1 = rand(); 
    std::cout << "Случайное число (0 - RAND_MAX): " << random_number1 << std::endl;

    // Случайное число от 1 до 100
    int random_number2 = rand() % 100 + 1; 
    std::cout << "Случайное число (1 - 100): " << random_number2 << std::endl;

    // Случайное число от 10 до 20
    int random_number3 = rand() % 11 + 10; // (max - min + 1) + min
    std::cout << "Случайное число (10 - 20): " << random_number3 << std::endl;

    return 0;
}
