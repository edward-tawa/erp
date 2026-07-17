// @/app/page.tsx
"use client";
import React from 'react';
import ProductCard from '@/components/inventory/ProductCard';
import { Product } from '@/types/inventory/product.types';

export default function Home() {
  const inventoryProducts: Product[] = [
    {
      id: 101,
      name: "Industrial Stainless Steel Valve",
      sku: "VAL-STEL-44X",
      price: 189.50,
      image: "https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=400&auto=format&fit=crop",
      category: {
        id: 1,
        name: "Mechanical Components",
        description: "Heavy duty manufacturing and industrial plumbing parts.",
        createdAt: "2026-01-01T00:00:00Z"
      },
      createdAt: "2026-01-15T08:00:00Z",
      UpdatedAt: "2026-03-22T14:30:00Z"
    },
    {
      id: 102,
      name: "Premium Ergonomic Workstation Chair",
      sku: "CHR-ERGO-997",
      price: 340.00,
      image: "https://images.unsplash.com/photo-1505797149-43b0069ec26b?q=80&w=400&auto=format&fit=crop",
      category: {
        id: 2,
        name: "Office Furniture",
        description: "Ergonomic seating and adaptive office desks.",
        createdAt: "2026-01-01T00:00:00Z"
      },
      createdAt: "2026-02-11T09:15:00Z",
      UpdatedAt: "2026-05-19T11:00:00Z"
    },
    {
      id: 103,
      name: "High-Speed Thermal Label Printer",
      sku: "PRN-THR-M20",
      price: 125.00,
      image: "",
      category: {
        id: 3,
        name: "Logistics Equipment",
        description: "Warehouse barcode tools, scales, and shipping peripherals.",
        createdAt: "2026-01-01T00:00:00Z"
      },
      createdAt: "2026-03-01T14:22:00Z",
      UpdatedAt: "2026-04-10T16:45:00Z"
    },
    {
      id: 104,
      name: "Cat6A Shielded Ethernet Cable (100ft)",
      sku: "CBL-C6AS-100",
      price: 42.99,
      image: "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?q=80&w=400&auto=format&fit=crop",
      category: {
        id: 4,
        name: "Networking",
        description: "High-bandwidth data infrastructure cables and switches.",
        createdAt: "2026-01-01T00:00:00Z"
      },
      createdAt: "2026-04-05T10:00:00Z",
      UpdatedAt: "2026-04-05T10:00:00Z"
    }
  ];

  const handleAddToCart = (product: Product) => {
    console.log(`Dispatched item to local storage / state context: ${product.name} (SKU: ${product.sku})`);
  };

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950 font-sans transition-colors duration-200">
      <main className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8 py-6 sm:py-8">

        {/* Workspace Title Header Section */}
        <div className="mb-6 sm:mb-8 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 border-b border-gray-200 dark:border-zinc-800 pb-5">
          <div>
            <h1 className="text-xl sm:text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50">
              Inventory Directory
            </h1>
            <p className="text-xs sm:text-sm text-zinc-500 dark:text-zinc-400 mt-1">
              Real-time monitoring and active product list management dashboard.
            </p>
          </div>
          <div className="text-[10px] sm:text-xs font-mono bg-zinc-200 dark:bg-zinc-800 text-zinc-700 dark:text-zinc-300 px-2.5 py-1 rounded-md self-start sm:self-center">
            Total Records: {inventoryProducts.length}
          </div>
        </div>

        {/* 
          FIX: 'grid-cols-2' forces 2 columns on mobile layout. 
          'gap-3 sm:gap-6' tightens padding on phones to preserve horizontal area.
        */}
        <div className="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3 sm:gap-6">
          {inventoryProducts.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onAddToCart={handleAddToCart}
            />
          ))}
        </div>

      </main>
    </div>
  );
}