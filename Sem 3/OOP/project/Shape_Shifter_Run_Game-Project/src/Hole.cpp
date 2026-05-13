#include "Hole.hpp"

Hole::Hole(HoleType holeType) : type(holeType)
{
    switch (holeType)
    {
        case HoleType::Circle: shape = std::make_unique<CircleShape>(50.f); break;
        case HoleType::Rectangle: shape = std::make_unique<RectShape>(sf::Vector2f(120.f, 60.f)); break;
        case HoleType::Triangle: shape = std::make_unique<TriangleShape>(); break;
    }
}

void Hole::setPosition(sf::Vector2f pos) { shape->setPosition(pos); }

void Hole::setScale(sf::Vector2f scale) { shape->setScale(scale); }

sf::FloatRect Hole::getBounds() const { return shape->getGlobalBounds(); }

sf::Vector2f Hole::getPosition() const { return shape->getPosition(); }

Shape* Hole::getShapePtr() const { return shape.get(); }