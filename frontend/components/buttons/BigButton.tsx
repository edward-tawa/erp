import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}

const BigButton: React.FC<ButtonProps> = ({ children, ...props }) => {
  return (
    <button
      {...props}
      className={`text-white hover:text-red-200 focus:outline-none focus:text-red-200 transition-all duration-200 transform hover:scale-105 ${props.className || ''
        }`}
    >
      {children}
    </button>
  );
};

export default BigButton;