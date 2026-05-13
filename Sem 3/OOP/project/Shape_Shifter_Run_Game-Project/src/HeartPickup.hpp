#ifndef HEARTPICKUP_HPP
#define HEARTPICKUP_HPP

#include <SFML/Graphics.hpp>

class HeartPickup
{
public:
    HeartPickup(sf::Vector2f pos);
    void update(float dt);
    void draw(sf::RenderWindow& window);
    sf::FloatRect getBounds() const;
    bool isOffScreen() const;
private:
    sf::CircleShape shape;
    sf::Vector2f velocity = {0.f, 160.f};
};

class FallingHeart
{
public:
    FallingHeart(sf::Vector2f startPos);
    void update(float dt);
    void draw(sf::RenderWindow& window) const;
    bool isFinished() const;
private:
    sf::CircleShape shape;
    sf::Vector2f velocity;
    float lifetime = 1.0f;
};

#endif // HEARTPICKUP_HPP