// @/components/category/CategoryCard.tsx
"use client";
import React from 'react';
import { Category } from '@/types/inventory/category.types';

interface CategoryCardProps {
    category: Category;
    onViewProducts?: (category: Category) => void;
}

const CategoryCard: React.FC<CategoryCardProps> = ({ category, onViewProducts }) => {
    const { id, name, description, createdAt } = category;

    // Optional timestamp helper formatting standard DB datetimes
    const formatDate = (isoString: string) => {
        try {
            return new Date(isoString).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'short',
                day: 'numeric',
            });
        } catch {
            return 'N/A';
        }
    };

    return (
        <div className="group bg-white rounded-xl border border-gray-200 p-5 shadow-sm hover:shadow-md transition-all duration-200 flex flex-col justify-between h-full">
            <div className="space-y-3">
                {/* ID & Timestamp Track Info */}
                <div className="flex items-center justify-between text-[11px] font-mono text-gray-400">
                    <span>ID: #{id}</span>
                    <span>Created: {formatDate(createdAt)}</span>
                </div>

                {/* Category Model Info */}
                <div className="space-y-1">
                    <h3 className="text-base font-bold text-gray-900 group-hover:text-red-600 transition-colors">
                        {name}
                    </h3>
                    <p className="text-xs text-gray-500 line-clamp-3 leading-relaxed">
                        {description || "No description provided for this backend model record."}
                    </p>
                </div>
            </div>

            {/* Action footer link */}
            {onViewProducts && (
                <div className="pt-4 mt-4 border-t border-gray-50">
                    <button
                        onClick={() => onViewProducts(category)}
                        className="text-xs font-semibold text-red-600 hover:text-red-700 inline-flex items-center gap-1.5 transition-colors focus:outline-none"
                    >
                        Browse Inventory Items
                        <svg className="w-3.5 h-3.5 stroke-current fill-none stroke-2 transition-transform group-hover:translate-x-0.5" viewBox="0 0 24 24">
                            <line x1="5" y1="12" x2="19" y2="12"></line>
                            <polyline points="12 5 19 12 12 19"></polyline>
                        </svg>
                    </button>
                </div>
            )}
        </div>
    );
};

export default CategoryCard;