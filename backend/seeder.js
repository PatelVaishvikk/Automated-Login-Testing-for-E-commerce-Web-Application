import mongoose from 'mongoose';
import dotenv from 'dotenv';
import Product from './models/productModel.js';
import data from './data.js';

dotenv.config();

mongoose
  .connect(process.env.MONGODB_URL || 'mongodb://localhost/amazona', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log('MongoDB connected for seeding'))
  .catch((err) => console.log('MongoDB connect error:', err));

const seed = async () => {
  try {
    await Product.deleteMany();
    const createdProducts = await Product.insertMany(data.products);
    console.log('Seed success:', createdProducts.length, 'products added');
    process.exit();
  } catch (error) {
    console.error('Seeding error:', error.message);
    process.exit(1);
  }
};

seed();
