#include <SFML/Graphics.hpp>

int main() {
    // Use initializer list for VideoMode
    sf::RenderWindow window(sf::VideoMode({800, 600}), "SFML Test");

    while (window.isOpen()) {
        // pollEvent now returns std::optional<sf::Event>
        while (const std::optional<sf::Event> event = window.pollEvent()) {
            if (event->is<sf::Event::Closed>()) {
                window.close();
            }
        }

        window.clear();
        window.display();
    }

    return 0;
}

