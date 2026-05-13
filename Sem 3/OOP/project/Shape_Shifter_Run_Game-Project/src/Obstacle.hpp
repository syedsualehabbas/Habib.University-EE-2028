#ifndef OBSTACLE_HPP
#define OBSTACLE_HPP

#include <SFML/Graphics.hpp>

class Obstacle
{
public:
    Obstacle(float wallY, float wallSpeed, float xPos);
    void update(float dt);
    void draw(sf::RenderWindow& window);
    bool isOffScreen() const;
    sf::FloatRect getBounds() const;
private:
    sf::RectangleShape obstacle;
    float speed;
};

#endif // OBSTACLE_HPP