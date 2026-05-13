#ifndef PLAYER_HPP
#define PLAYER_HPP

#include <SFML/Graphics.hpp>
#include <memory>
#include "Shape.hpp"

class Player
{
public:
    enum class ShapeType { Circle, Rectangle, Triangle };
    Player() : shape(std::make_unique<RectShape>()), velocity({0.f, 0.f}), lastShapeType(ShapeType::Rectangle)
    {
        shape->setPosition({400.f, 525.f});
        alignWithPlatform();
    }
    void handleInput();
    void changeShape(ShapeType type);
    void update(float dt);
    void draw(sf::RenderWindow& window);
    sf::FloatRect getBounds() const;
    sf::Vector2f getPosition() const;
    ShapeType getCurrentShapeType() const { return lastShapeType; }
private:
    void alignWithPlatform();
    std::unique_ptr<Shape> shape;
    sf::Vector2f velocity;
    float speed = 500.f;
    float platformLeft = 120.f;
    float platformRight = 680.f;
    float platformTop = 550.f;
    sf::Clock shapeChangeClock;
    ShapeType lastShapeType;
};

#endif // PLAYER_HPP