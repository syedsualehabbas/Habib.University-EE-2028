#ifndef SHAPE_HPP
#define SHAPE_HPP

#include <SFML/Graphics.hpp>
#include <memory>

// ========== BASE SHAPE CLASS ==========
class Shape : public sf::Drawable
{
public:
    virtual ~Shape() = default;
    virtual sf::FloatRect getGlobalBounds() const = 0;
    virtual void setPosition(sf::Vector2f pos) = 0;
    virtual sf::Vector2f getPosition() const = 0;
    virtual void setScale(sf::Vector2f scale) = 0;
    virtual void draw(sf::RenderTarget& target, sf::RenderStates states) const = 0;
};

class CircleShape : public Shape
{
private:
    sf::CircleShape shape;
public:
    CircleShape(float radius = 40.f) : shape(radius)
    {
        shape.setOrigin({radius, radius});
        shape.setFillColor(sf::Color(100, 200, 255));
    }
    sf::FloatRect getGlobalBounds() const override { return shape.getGlobalBounds(); }
    void setPosition(sf::Vector2f pos) override { shape.setPosition(pos); }
    sf::Vector2f getPosition() const override { return shape.getPosition(); }
    void setScale(sf::Vector2f scale) override { shape.setScale(scale); }
    void draw(sf::RenderTarget& target, sf::RenderStates states) const override { target.draw(shape, states); }
};

class RectShape : public Shape
{
private:
    sf::RectangleShape shape;
public:
    RectShape(sf::Vector2f size = {100.f, 50.f}) : shape(size)
    {
        shape.setOrigin({size.x / 2.f, size.y / 2.f});
        shape.setFillColor(sf::Color(255, 150, 100));
    }
    sf::FloatRect getGlobalBounds() const override { return shape.getGlobalBounds(); }
    void setPosition(sf::Vector2f pos) override { shape.setPosition(pos); }
    sf::Vector2f getPosition() const override { return shape.getPosition(); }
    void setScale(sf::Vector2f scale) override { shape.setScale(scale); }
    void draw(sf::RenderTarget& target, sf::RenderStates states) const override { target.draw(shape, states); }
};

class TriangleShape : public Shape
{
private:
    sf::ConvexShape shape;
public:
    TriangleShape() : shape(3)
    {
        shape.setPoint(0, {0.f, -50.f});
        shape.setPoint(1, {-50.f, 50.f});
        shape.setPoint(2, {50.f, 50.f});
        shape.setFillColor(sf::Color(100, 255, 150));
        shape.setOrigin({0.f, 0.f});
    }
    sf::FloatRect getGlobalBounds() const override { return shape.getGlobalBounds(); }
    void setPosition(sf::Vector2f pos) override { shape.setPosition(pos); }
    sf::Vector2f getPosition() const override { return shape.getPosition(); }
    void setScale(sf::Vector2f scale) override { shape.setScale(scale); }
    void draw(sf::RenderTarget& target, sf::RenderStates states) const override { target.draw(shape, states); }
};

#endif // SHAPE_HPP