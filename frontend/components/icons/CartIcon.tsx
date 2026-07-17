import React from 'react';
import { IconProps } from '@/types/components/icons/carticon.types';

const CartIcon: React.FC<IconProps> = ({
    size = 20, // Default fallback size (5 = 20px in Tailwind's w-5 h-5 scale)
    className = '',
    ...props
}) => {
    return (
        <svg
            width={size}
            height={size}
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={`stroke-current ${className}`}
            {...props}
        >
            <circle cx="9" cy="21" r="1" />
            <circle cx="20" cy="21" r="1" />
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6" />
        </svg>
    );
};

export default CartIcon;