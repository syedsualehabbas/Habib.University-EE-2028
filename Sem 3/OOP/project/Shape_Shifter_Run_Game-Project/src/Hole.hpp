#ifndef HOLE_HPP
#define HOLE_HPP

#include <SFML/Graphics.hpp>
#include <memory>
#include "Shape.hpp"

class Hole
{
public:
    enum class HoleType { Circle, Rectangle, Triangle };
    HoleType type;
    Hole(HoleType holeType);
    void setPosition(sf::Vector2f pos);
    void setScale(sf::Vector2f scale);
    sf::FloatRect getBounds() const;
    sf::Vector2f getPosition() const;
    Shape* getShapePtr() const;
private:
    std::unique_ptr<Shape> shape;
};

#endif // HOLE_HPP