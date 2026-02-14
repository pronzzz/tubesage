import React from 'react';
import { motion } from 'framer-motion';

const GlassCard = ({ children, className = '', delay = 0 }) => {
    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay }}
            className={`backdrop-blur-md bg-white/10 border border-white/20 rounded-xl p-6 shadow-xl ${className}`}
        >
            {children}
        </motion.div>
    );
};

export default GlassCard;
