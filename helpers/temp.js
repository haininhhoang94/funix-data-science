class Particle {
  constructor(x, y) {
    this.position = createVector(x, y);
    this.velocity = createVector(0, 0);
    this.acceleration = createVector(0, 0);
  }
  applyForce(force) {
    this.acceleration.add(force);
  }
  update() {
    this.velocity.add(this.acceleration);
    this.position.add(this.velocity);
    this.acceleration.mult(0);
  }
  display() {
    fill(255);
    ellipse(this.position.x, this.position.y, 10, 10);
  }
}
class ParticleSystem {
  constructor() {
    this.particles = [];
    this.G = 0.5;
  }
  addParticle(x, y) {
    this.particles.push(new Particle(x, y));
  }
  run() {
    for (const p of this.particles) {
      p.update();
      p.display();
    }
  }
  applyForces() {
    for (let i = 0; i < this.particles.length; i++) {
      for (let j = i + 1; j < this.particles.length; j++) {
        const particleA = this.particles[i];
        const particleB = this.particles[j];
        const force = p5.Vector.sub(particleB.position, particleA.position);
        const distanceSq = force.magSq();
        const strength = (this.G * particleA.mass * particleB.mass) / distanceSq;
        force.setMag(strength);
        particleA.applyForce(force);
        particleB.applyForce(force.mult(-1));
      }
    }
  }
}
let particleSystem;
function setup() {
  createCanvas(400, 400);
  particleSystem = new ParticleSystem();
  // Add particles to the system
  particleSystem.addParticle(100, 100);
  particleSystem.addParticle(200, 200);
  particleSystem.addParticle(300, 300);
}
function draw() {
  background(0);

  // Apply forces to the particles
  particleSystem.applyForces();
  // Run the particle system
  particleSystem.run();
}
