#include "Obstacle.hpp"
#include <cstdlib>

Obstacle::Obstacle(float wallY, float wallSpeed, float xPos) : speed(wallSpeed)
{
    float width = 60.f + static_cast<float>(rand() % 40);
    float height = 60.f + static_cast<float>(rand() % 40);
    obstacle.setSize({width, height});
    obstacle.setOrigin({width / 2.f, height / 2.f});
    obstacle.setFillColor(sf::Color(255, 50, 50));
    obstacle.setOutlineColor(sf::Color(200, 0, 0));
    obstacle.setOutlineThickness(3.f);
    obstacle.setPosition({xPos, wallY});
}

void Obstacle::update(float dt) { obstacle.move({0.f, speed * dt}); }

void Obstacle::draw(sf::RenderWindow& window) { window.draw(obstacle); }

bool Obstacle::isOffScreen() const { return obstacle.getPosition().y > 650.f; }

sf::FloatRect Obstacle::getBounds() const { return obstacle.getGlobalBounds(); }