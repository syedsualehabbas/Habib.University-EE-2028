#include "HeartPickup.hpp"
#include <cmath>

HeartPickup::HeartPickup(sf::Vector2f pos)
{
    shape.setRadius(14.f);
    shape.setOrigin({14.f, 14.f});
    shape.setFillColor(sf::Color(255, 120, 160));
    shape.setPosition(pos);
}

void HeartPickup::update(float dt) { shape.move(velocity * dt); }

void HeartPickup::draw(sf::RenderWindow& window) { window.draw(shape); }

sf::FloatRect HeartPickup::getBounds() const { return shape.getGlobalBounds(); }

bool HeartPickup::isOffScreen() const { return shape.getPosition().y > 620.f; }

FallingHeart::FallingHeart(sf::Vector2f startPos)
{
    shape.setRadius(8.f);
    shape.setOrigin({8.f, 8.f});
    shape.setFillColor(sf::Color(255, 100, 150));
    shape.setPosition(startPos);
    velocity = {0.f, 180.f};
}

void FallingHeart::update(float dt)
{
    shape.move(velocity * dt);
    lifetime -= dt;
    if (lifetime < 0.f) lifetime = 0.f;
    sf::Color c = shape.getFillColor();
    c.a = static_cast<std::uint8_t>(255.f * lifetime);
    shape.setFillColor(c);
}

void FallingHeart::draw(sf::RenderWindow& window) const { window.draw(shape); }

bool FallingHeart::isFinished() const { return lifetime <= 0.f || shape.getPosition().y > 620.f; }