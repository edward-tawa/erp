// @/components/product/ProductCard.tsx
"use client";
import React from 'react';
import { Product } from '@/types/inventory/product.types';
import CartIcon from '@/components/icons/CartIcon';

interface ProductCardProps {
    product: Product;
    onAddToCart?: (product: Product) => void;
}

const ProductCard: React.FC<ProductCardProps> = ({ product, onAddToCart }) => {
    const { name, price, category, image, sku } = product;

    const formatCurrency = (value: number) => {
        return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(value);
    };

    return (
        <div className="group bg-white rounded-xl border border-gray-200 shadow-sm hover:shadow-md transition-all duration-200 overflow-hidden flex flex-col w-full h-full">

            {/* 
              1. Fixed Image Box
              'aspect-square' plus 'w-full' locks the width and height to perfectly match.
              'flex-shrink-0' keeps the image container from compressing.
            */}
            <div className="relative aspect-square w-full bg-gray-100 flex items-center justify-center flex-shrink-0 overflow-hidden">
                {image ? (
                    <img
                        src={image}
                        alt={name}
                        className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-300"
                    />
                ) : (
                    <svg className="w-8 h-8 sm:w-12 sm:h-12 text-gray-300 fill-none stroke-1" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                    </svg>
                )}
                {sku && (
                    <span className="absolute top-1.5 left-1.5 bg-gray-900/70 text-white text-[9px] sm:text-[10px] font-mono px-1.5 py-0.5 rounded tracking-tight">
                        {sku}
                    </span>
                )}
            </div>

            {/* 
              2. Content Box
              Using 'flex-grow justify-between' means if one product name takes 1 line
              and another takes 2 lines, the pricing footer is pinned to the bottom.
            */}
            <div className="p-3 sm:p-4 flex flex-col flex-grow justify-between gap-2 sm:gap-3">
                <div className="space-y-0.5 sm:space-y-1">
                    {category?.name && (
                        <span
                            title={category.description}
                            className="text-[10px] sm:text-xs font-semibold text-red-600 uppercase tracking-wider cursor-help block truncate"
                        >
                            {category.name}
                        </span>
                    )}
                    {/* 'line-clamp-2' allocates space for exactly up to two text lines */}
                    <h3 className="font-semibold text-gray-800 text-xs sm:text-sm md:text-base line-clamp-2 leading-tight group-hover:text-red-600 transition-colors min-h-[2rem] sm:min-h-[2.5rem]">
                        {name}
                    </h3>
                </div>

                {/* Pricing & Cart Action Row - Pushed down evenly via 'mt-auto' */}
                <div className="flex items-center justify-between pt-1.5 sm:pt-2 border-t border-gray-50 mt-auto flex-shrink-0">
                    <span className="text-sm sm:text-base md:text-lg font-bold text-gray-900">
                        {formatCurrency(price)}
                    </span>
                    {onAddToCart && (
                        <button
                            onClick={() => onAddToCart(product)}
                            className="p-1.5 sm:p-2 rounded-lg bg-red-50 text-red-600 hover:bg-red-600 hover:text-white transition-all active:scale-95 shadow-xs flex-shrink-0"
                            aria-label="Add to cart"
                        >
                            <CartIcon size={14} className="sm:w-4 sm:h-4" />
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ProductCard;