#include "Player.hpp"

void Player::handleInput()
{
    velocity.x = 0.f;
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Left) || sf::Keyboard::isKeyPressed(sf::Keyboard::Key::A))
        velocity.x = -speed;
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Right) || sf::Keyboard::isKeyPressed(sf::Keyboard::Key::D))
        velocity.x = speed;
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Num1))
        changeShape(ShapeType::Circle);
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Num2))
        changeShape(ShapeType::Rectangle);
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Num3))
        changeShape(ShapeType::Triangle);
}

void Player::changeShape(ShapeType type)
{
    if (shapeChangeClock.getElapsedTime().asMilliseconds() < 200 || lastShapeType == type)
        return;
    sf::Vector2f currentPos = shape->getPosition();
    switch (type)
    {
        case ShapeType::Circle: shape = std::make_unique<CircleShape>(); break;
        case ShapeType::Rectangle: shape = std::make_unique<RectShape>(); break;
        case ShapeType::Triangle: shape = std::make_unique<TriangleShape>(); break;
    }
    lastShapeType = type;
    shape->setPosition(currentPos);
    alignWithPlatform();
    shapeChangeClock.restart();
}

void Player::update(float dt)
{
    sf::Vector2f currentPos = shape->getPosition();
    currentPos.x += velocity.x * dt;
    if (currentPos.x < platformLeft) currentPos.x = platformLeft;
    if (currentPos.x > platformRight) currentPos.x = platformRight;
    shape->setPosition(currentPos);
    alignWithPlatform();
}

void Player::draw(sf::RenderWindow& window) { window.draw(*shape); }

sf::FloatRect Player::getBounds() const { return shape->getGlobalBounds(); }

sf::Vector2f Player::getPosition() const { return shape->getPosition(); }

void Player::alignWithPlatform()
{
    sf::FloatRect bounds = shape->getGlobalBounds();
    float bottom = bounds.position.y + bounds.size.y;
    float dy = platformTop - bottom;
    sf::Vector2f pos = shape->getPosition();
    pos.y += dy;
    shape->setPosition(pos);
}