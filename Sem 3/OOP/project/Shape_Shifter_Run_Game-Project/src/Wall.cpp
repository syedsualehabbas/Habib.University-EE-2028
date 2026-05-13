#include "Wall.hpp"
#include <cstdlib>
#include <cmath>
#include <algorithm>

Wall::Wall(Hole::HoleType holeType, float wallSpeed) : hole(std::make_unique<Hole>(holeType)), speed(wallSpeed)
{
    wall.setSize({800.f, 100.f});
    int colorChoice = rand() % 4;
    switch(colorChoice)
    {
        case 0: wallColor = sf::Color(255, 100, 100); break;
        case 1: wallColor = sf::Color(100, 255, 100); break;
        case 2: wallColor = sf::Color(100, 100, 255); break;
        case 3: wallColor = sf::Color(255, 200, 100); break;
    }
    wall.setFillColor(wallColor);
    wall.setPosition({0.f, -100.f});
    float holeOffsetX = static_cast<float>((rand() % 600) + 100);
    hole->setPosition({holeOffsetX, -100.f});
    hole->setScale({1.0f, 1.0f});
}

void Wall::update(float dt)
{
    wall.move({0.f, speed * dt});
    sf::Vector2f wallPos = wall.getPosition();
    sf::Vector2f holePos = hole->getPosition();
    holePos.y = wallPos.y + 50.f;
    hole->setPosition(holePos);
}

void Wall::draw(sf::RenderWindow& window)
{
    static sf::RenderTexture rt({800, 600});

    float y = wall.getPosition().y;
    sf::Color fadedColor = wallColor;
    if (y > 380.f)
    {
        float t = std::min((y - 380.f) / 170.f, 1.0f);
        fadedColor.a = static_cast<std::uint8_t>(255.f * (1.f - t));
    }
    wall.setFillColor(fadedColor);

    rt.clear(sf::Color::Transparent);
    rt.draw(wall);
    sf::BlendMode cutoutBlend(sf::BlendMode::Factor::Zero, sf::BlendMode::Factor::OneMinusSrcAlpha,
        sf::BlendMode::Equation::Add, sf::BlendMode::Factor::Zero, sf::BlendMode::Factor::OneMinusSrcAlpha,
        sf::BlendMode::Equation::Add);
    rt.draw(*hole->getShapePtr(), sf::RenderStates(cutoutBlend));
    rt.display();
    sf::Sprite finalSprite(rt.getTexture());
    window.draw(finalSprite);
}

bool Wall::isOffScreen() const { return wall.getPosition().y >= 550.f; }

sf::FloatRect Wall::getWallBounds() const { return wall.getGlobalBounds(); }

sf::FloatRect Wall::getHoleBounds() const { return hole->getBounds(); }

Hole::HoleType Wall::getHoleType() const { return hole->type; }

float Wall::getWallY() const { return wall.getPosition().y; }