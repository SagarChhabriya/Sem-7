"""
Comprehensive visualization script for CNN, Shallow Methods, and GCNN results
Research paper quality visualizations with proper formatting
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from pathlib import Path
import seaborn as sns

# Set publication-quality style
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.linewidth': 1.2,
    'grid.linewidth': 0.8,
    'lines.linewidth': 2,
    'patch.linewidth': 1.2
})

# Color palette for research paper
COLORS = {
    'cnn': '#2E86AB',      # Blue
    'gcnn': '#A23B72',     # Purple
    'shallow': '#F18F01',   # Orange
    'train': '#06A77D',    # Green
    'test': '#D00000',     # Red
    'perfect': '#000000'   # Black
}

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

def extract_epoch_from_filename(filename):
    """Extract epoch number from filename"""
    match = re.search(r'epoch(\d+)', filename)
    return int(match.group(1)) if match else None

def load_cnn_results():
    """Load CNN training results"""
    csv_path = '../training_results_cnn.csv'
    if not os.path.exists(csv_path):
        print("Warning: training_results_cnn.csv not found")
        return None
    
    df = pd.read_csv(csv_path)
    df['epoch'] = range(1, len(df) + 1)
    print(f"Loaded CNN results: {len(df)} epochs")
    return df

def load_shallow_methods_results():
    """Load shallow methods results"""
    csv_path = '../results_shallow_methods.csv'
    if not os.path.exists(csv_path):
        print("Warning: results_shallow_methods.csv not found")
        return None
    
    df = pd.read_csv(csv_path)
    print(f"Loaded shallow methods results: {len(df)} models")
    return df

def load_gcnn_results():
    """Load GCNN results from results directory"""
    results_dir = Path('../results')
    if not results_dir.exists():
        print("Warning: results/ directory not found")
        return None
    
    epochs = set()
    for file in results_dir.glob('*.csv'):
        epoch = extract_epoch_from_filename(file.name)
        if epoch is not None:
            epochs.add(epoch)
    
    epochs = sorted(list(epochs))
    print(f"Found {len(epochs)} GCNN epochs")
    
    gcnn_data = []
    for epoch in epochs:
        try:
            pred_test = np.loadtxt(f'../results/gcnn_pred_test_m_epoch{epoch}.csv')
            actual_test = np.loadtxt(f'../results/gcnn_actual_test_m_epoch{epoch}.csv')
            pred_train = np.loadtxt(f'../results/gcnn_pred_train_m_epoch{epoch}.csv')
            actual_train = np.loadtxt(f'../results/gcnn_actual_train_m_epoch{epoch}.csv')
            
            test_mse = np.mean((pred_test - actual_test)**2)
            train_mse = np.mean((pred_train - actual_train)**2)
            test_r2 = 1 - np.sum((actual_test - pred_test)**2) / np.sum((actual_test - np.mean(actual_test))**2)
            train_r2 = 1 - np.sum((actual_train - pred_train)**2) / np.sum((actual_train - np.mean(actual_train))**2)
            test_mae = np.mean(np.abs(pred_test - actual_test))
            train_mae = np.mean(np.abs(pred_train - actual_train))
            
            gcnn_data.append({
                'epoch': epoch,
                'test_mse': test_mse,
                'train_mse': train_mse,
                'test_r2': test_r2,
                'train_r2': train_r2,
                'test_mae': test_mae,
                'train_mae': train_mae,
                'pred_test': pred_test,
                'actual_test': actual_test,
                'pred_train': pred_train,
                'actual_train': actual_train
            })
        except Exception as e:
            print(f"Warning: Could not load epoch {epoch}: {e}")
            continue
    
    return pd.DataFrame([{k: v for k, v in d.items() if k not in ['pred_test', 'actual_test', 'pred_train', 'actual_train']} 
                        for d in gcnn_data]) if gcnn_data else None, gcnn_data

# ============================================================================
# CNN VISUALIZATIONS
# ============================================================================

def visualize_cnn_individual(cnn_df):
    """Create individual visualizations for CNN"""
    if cnn_df is None:
        return
    
    # Figure 1: Training curves
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('CNN Training Progress', fontsize=16, fontweight='bold', y=0.995)
    
    # R² over epochs
    ax1 = axes[0, 0]
    ax1.plot(cnn_df['epoch'], cnn_df['train_r2'], label='Train R²', 
             color=COLORS['train'], marker='o', markersize=3, linewidth=2, alpha=0.8)
    ax1.plot(cnn_df['epoch'], cnn_df['test_r2'], label='Test R²', 
             color=COLORS['test'], marker='s', markersize=3, linewidth=2, alpha=0.8)
    ax1.set_xlabel('Epoch', fontweight='bold')
    ax1.set_ylabel('R² Score', fontweight='bold')
    ax1.set_title('(a) R² Score vs Epoch', fontweight='bold')
    ax1.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_xlim(left=0)
    
    # Loss over epochs
    ax2 = axes[0, 1]
    ax2.plot(cnn_df['epoch'], cnn_df['train_loss'], label='Train Loss', 
             color=COLORS['train'], marker='o', markersize=3, linewidth=2, alpha=0.8)
    ax2.plot(cnn_df['epoch'], cnn_df['test_loss'], label='Test Loss', 
             color=COLORS['test'], marker='s', markersize=3, linewidth=2, alpha=0.8)
    ax2.set_xlabel('Epoch', fontweight='bold')
    ax2.set_ylabel('Loss', fontweight='bold')
    ax2.set_title('(b) Loss vs Epoch', fontweight='bold')
    ax2.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.set_xlim(left=0)
    
    # Best performance summary
    ax3 = axes[1, 0]
    best_epoch_idx = cnn_df['test_r2'].idxmax()
    best_epoch = cnn_df.loc[best_epoch_idx]
    
    metrics = ['train_r2', 'test_r2', 'train_loss', 'test_loss']
    values = [best_epoch[m] for m in metrics]
    labels = ['Train R²', 'Test R²', 'Train Loss', 'Test Loss']
    colors_bar = [COLORS['train'], COLORS['test'], COLORS['train'], COLORS['test']]
    
    bars = ax3.barh(labels, values, color=colors_bar, alpha=0.7, edgecolor='black', linewidth=1.5)
    ax3.set_xlabel('Value', fontweight='bold')
    ax3.set_title(f'(c) Best Epoch ({int(best_epoch["epoch"])}) Metrics', fontweight='bold')
    ax3.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add value labels
    for bar, val in zip(bars, values):
        width = bar.get_width()
        ax3.text(width, bar.get_y() + bar.get_height()/2, 
                f'{val:.4f}', ha='left' if width > 0 else 'right', 
                va='center', fontweight='bold', fontsize=9)
    
    # Performance distribution
    ax4 = axes[1, 1]
    ax4.hist(cnn_df['test_r2'], bins=30, color=COLORS['test'], alpha=0.6, edgecolor='black', label='Test R²')
    ax4.hist(cnn_df['train_r2'], bins=30, color=COLORS['train'], alpha=0.6, edgecolor='black', label='Train R²')
    ax4.axvline(cnn_df['test_r2'].max(), color='red', linestyle='--', linewidth=2, label='Best Test R²')
    ax4.set_xlabel('R² Score', fontweight='bold')
    ax4.set_ylabel('Frequency', fontweight='bold')
    ax4.set_title('(d) R² Score Distribution', fontweight='bold')
    ax4.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax4.grid(True, alpha=0.3, linestyle='--', axis='y')
    
    plt.tight_layout(rect=[0, 0, 1, 0.99])
    plt.savefig('cnn_individual_results.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Saved cnn_individual_results.png")
    plt.close()

# ============================================================================
# SHALLOW METHODS VISUALIZATIONS
# ============================================================================

def visualize_shallow_methods_individual(shallow_df):
    """Create individual visualizations for shallow methods"""
    if shallow_df is None or len(shallow_df) == 0:
        return
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Shallow Learning Methods Performance', fontsize=16, fontweight='bold', y=0.995)
    
    models = shallow_df['model'].unique()
    n_models = len(models)
    x_pos = np.arange(n_models)
    colors = [COLORS['shallow']] * n_models
    
    # Test R² comparison
    ax1 = axes[0, 0]
    test_r2_means = [shallow_df[shallow_df['model'] == m]['test_r2_mean'].values[0] for m in models]
    test_r2_stds = [shallow_df[shallow_df['model'] == m]['test_r2_std'].values[0] for m in models]
    bars = ax1.bar(x_pos, test_r2_means, yerr=test_r2_stds, capsize=8, 
                   color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_xlabel('Model', fontweight='bold')
    ax1.set_ylabel('Test R² Score', fontweight='bold')
    ax1.set_title('(a) Test R² by Model', fontweight='bold')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(models, rotation=45, ha='right')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    ax1.set_ylim(bottom=0)
    
    # Add value labels
    for bar, val, std in zip(bars, test_r2_means, test_r2_stds):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + std + 0.01,
                f'{val:.4f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
    
    # Test MSE comparison
    ax2 = axes[0, 1]
    test_mse_means = [shallow_df[shallow_df['model'] == m]['test_mse_mean'].values[0] for m in models]
    test_mse_stds = [shallow_df[shallow_df['model'] == m]['test_mse_std'].values[0] for m in models]
    bars2 = ax2.bar(x_pos, test_mse_means, yerr=test_mse_stds, capsize=8,
                    color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_xlabel('Model', fontweight='bold')
    ax2.set_ylabel('Test MSE', fontweight='bold')
    ax2.set_title('(b) Test MSE by Model', fontweight='bold')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(models, rotation=45, ha='right')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Train vs Test R²
    ax3 = axes[1, 0]
    train_r2_means = [shallow_df[shallow_df['model'] == m]['train_r2_mean'].values[0] for m in models]
    width = 0.35
    bars3a = ax3.bar(x_pos - width/2, train_r2_means, width, label='Train R²', 
                     color=COLORS['train'], alpha=0.8, edgecolor='black', linewidth=1.5)
    bars3b = ax3.bar(x_pos + width/2, test_r2_means, width, label='Test R²', 
                     color=COLORS['test'], alpha=0.8, edgecolor='black', linewidth=1.5)
    ax3.set_xlabel('Model', fontweight='bold')
    ax3.set_ylabel('R² Score', fontweight='bold')
    ax3.set_title('(c) Train vs Test R²', fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(models, rotation=45, ha='right')
    ax3.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax3.grid(axis='y', alpha=0.3, linestyle='--')
    ax3.set_ylim(bottom=0)
    
    # Train vs Test MSE
    ax4 = axes[1, 1]
    train_mse_means = [shallow_df[shallow_df['model'] == m]['train_mse_mean'].values[0] for m in models]
    bars4a = ax4.bar(x_pos - width/2, train_mse_means, width, label='Train MSE', 
                     color=COLORS['train'], alpha=0.8, edgecolor='black', linewidth=1.5)
    bars4b = ax4.bar(x_pos + width/2, test_mse_means, width, label='Test MSE', 
                     color=COLORS['test'], alpha=0.8, edgecolor='black', linewidth=1.5)
    ax4.set_xlabel('Model', fontweight='bold')
    ax4.set_ylabel('MSE', fontweight='bold')
    ax4.set_title('(d) Train vs Test MSE', fontweight='bold')
    ax4.set_xticks(x_pos)
    ax4.set_xticklabels(models, rotation=45, ha='right')
    ax4.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax4.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout(rect=[0, 0, 1, 0.99])
    plt.savefig('shallow_methods_individual_results.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Saved shallow_methods_individual_results.png")
    plt.close()

# ============================================================================
# GCNN VISUALIZATIONS
# ============================================================================

def visualize_gcnn_individual(gcnn_df, gcnn_data):
    """Create individual visualizations for GCNN"""
    if gcnn_df is None or len(gcnn_df) == 0:
        return
    
    # Figure 1: Training curves
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('GCNN Training Progress', fontsize=16, fontweight='bold', y=0.995)
    
    # R² over epochs
    ax1 = axes[0, 0]
    ax1.plot(gcnn_df['epoch'], gcnn_df['train_r2'], label='Train R²', 
             color=COLORS['train'], marker='o', markersize=3, linewidth=2, alpha=0.8)
    ax1.plot(gcnn_df['epoch'], gcnn_df['test_r2'], label='Test R²', 
             color=COLORS['test'], marker='s', markersize=3, linewidth=2, alpha=0.8)
    ax1.set_xlabel('Epoch', fontweight='bold')
    ax1.set_ylabel('R² Score', fontweight='bold')
    ax1.set_title('(a) R² Score vs Epoch', fontweight='bold')
    ax1.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # MSE over epochs
    ax2 = axes[0, 1]
    ax2.plot(gcnn_df['epoch'], gcnn_df['train_mse'], label='Train MSE', 
             color=COLORS['train'], marker='o', markersize=3, linewidth=2, alpha=0.8)
    ax2.plot(gcnn_df['epoch'], gcnn_df['test_mse'], label='Test MSE', 
             color=COLORS['test'], marker='s', markersize=3, linewidth=2, alpha=0.8)
    ax2.set_xlabel('Epoch', fontweight='bold')
    ax2.set_ylabel('MSE', fontweight='bold')
    ax2.set_title('(b) MSE vs Epoch', fontweight='bold')
    ax2.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # MAE over epochs
    ax3 = axes[1, 0]
    ax3.plot(gcnn_df['epoch'], gcnn_df['train_mae'], label='Train MAE', 
             color=COLORS['train'], marker='o', markersize=3, linewidth=2, alpha=0.8)
    ax3.plot(gcnn_df['epoch'], gcnn_df['test_mae'], label='Test MAE', 
             color=COLORS['test'], marker='s', markersize=3, linewidth=2, alpha=0.8)
    ax3.set_xlabel('Epoch', fontweight='bold')
    ax3.set_ylabel('MAE', fontweight='bold')
    ax3.set_title('(c) MAE vs Epoch', fontweight='bold')
    ax3.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax3.grid(True, alpha=0.3, linestyle='--')
    
    # Best epoch summary
    ax4 = axes[1, 1]
    best_epoch_idx = gcnn_df['test_r2'].idxmax()
    best_epoch = gcnn_df.loc[best_epoch_idx]
    
    metrics = ['test_mse', 'test_r2', 'test_mae', 'train_mse', 'train_r2', 'train_mae']
    values = [best_epoch[m] for m in metrics]
    labels = ['Test MSE', 'Test R²', 'Test MAE', 'Train MSE', 'Train R²', 'Train MAE']
    colors_bar = [COLORS['test'], COLORS['test'], COLORS['test'], 
                  COLORS['train'], COLORS['train'], COLORS['train']]
    
    bars = ax4.barh(labels, values, color=colors_bar, alpha=0.7, edgecolor='black', linewidth=1.5)
    ax4.set_xlabel('Value', fontweight='bold')
    ax4.set_title(f'(d) Best Epoch ({int(best_epoch["epoch"])}) Metrics', fontweight='bold')
    ax4.grid(axis='x', alpha=0.3, linestyle='--')
    
    plt.tight_layout(rect=[0, 0, 1, 0.99])
    plt.savefig('gcnn_individual_results.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Saved gcnn_individual_results.png")
    plt.close()
    
    # Figure 2: Prediction scatter plots
    if gcnn_data:
        epochs_to_plot = [gcnn_data[0]['epoch'], 
                          gcnn_data[len(gcnn_data)//2]['epoch'],
                          gcnn_data[-1]['epoch']]
        plot_data = [d for d in gcnn_data if d['epoch'] in epochs_to_plot]
        
        if plot_data:
            fig, axes = plt.subplots(len(plot_data), 2, figsize=(14, 5*len(plot_data)))
            if len(plot_data) == 1:
                axes = axes.reshape(1, -1)
            fig.suptitle('GCNN Predictions vs Actual Values', fontsize=16, fontweight='bold', y=0.995)
            
            for idx, data in enumerate(plot_data):
                epoch = data['epoch']
                
                # Test set
                ax1 = axes[idx, 0]
                pred_test = data['pred_test']
                actual_test = data['actual_test']
                
                ax1.scatter(actual_test, pred_test, alpha=0.6, s=15, 
                           edgecolors='black', linewidths=0.2, color=COLORS['gcnn'])
                
                min_val = min(actual_test.min(), pred_test.min())
                max_val = max(actual_test.max(), pred_test.max())
                ax1.plot([min_val, max_val], [min_val, max_val], 
                        color=COLORS['perfect'], linestyle='--', linewidth=2, 
                        label='Perfect Prediction', zorder=10)
                
                ax1.set_xlabel('Actual Value', fontweight='bold')
                ax1.set_ylabel('Predicted Value', fontweight='bold')
                ax1.set_title(f'Test Set - Epoch {epoch} (R² = {data["test_r2"]:.4f})', fontweight='bold')
                ax1.legend(loc='best', frameon=True, fancybox=True, shadow=True)
                ax1.grid(True, alpha=0.3, linestyle='--')
                ax1.set_aspect('equal', adjustable='box')
                
                # Train set
                ax2 = axes[idx, 1]
                pred_train = data['pred_train']
                actual_train = data['actual_train']
                
                ax2.scatter(actual_train, pred_train, alpha=0.6, s=15, 
                           edgecolors='black', linewidths=0.2, color=COLORS['gcnn'])
                min_val = min(actual_train.min(), pred_train.min())
                max_val = max(actual_train.max(), pred_train.max())
                ax2.plot([min_val, max_val], [min_val, max_val], 
                        color=COLORS['perfect'], linestyle='--', linewidth=2, 
                        label='Perfect Prediction', zorder=10)
                
                ax2.set_xlabel('Actual Value', fontweight='bold')
                ax2.set_ylabel('Predicted Value', fontweight='bold')
                ax2.set_title(f'Train Set - Epoch {epoch} (R² = {data["train_r2"]:.4f})', fontweight='bold')
                ax2.legend(loc='best', frameon=True, fancybox=True, shadow=True)
                ax2.grid(True, alpha=0.3, linestyle='--')
                ax2.set_aspect('equal', adjustable='box')
            
            plt.tight_layout(rect=[0, 0, 1, 0.99])
            plt.savefig('gcnn_predictions_scatter.png', dpi=300, bbox_inches='tight', facecolor='white')
            print("Saved gcnn_predictions_scatter.png")
            plt.close()

# ============================================================================
# COMBINED COMPARISON VISUALIZATIONS
# ============================================================================

def visualize_combined_comparison(cnn_df, shallow_df, gcnn_df):
    """Create combined comparison visualizations"""
    if cnn_df is None and shallow_df is None and gcnn_df is None:
        return
    
    # Prepare best results
    results = {}
    
    if cnn_df is not None:
        best_cnn = cnn_df.loc[cnn_df['test_r2'].idxmax()]
        results['CNN'] = {
            'test_r2': best_cnn['test_r2'],
            'test_mse': best_cnn['test_loss'],
            'train_r2': best_cnn['train_r2'],
            'train_mse': best_cnn['train_loss']
        }
    
    if shallow_df is not None and len(shallow_df) > 0:
        for _, row in shallow_df.iterrows():
            model_name = f"Shallow ({row['model']})"
            results[model_name] = {
                'test_r2': row['test_r2_mean'],
                'test_mse': row['test_mse_mean'],
                'train_r2': row['train_r2_mean'],
                'train_mse': row['train_mse_mean']
            }
    
    if gcnn_df is not None and len(gcnn_df) > 0:
        best_gcnn = gcnn_df.loc[gcnn_df['test_r2'].idxmax()]
        results['GCNN'] = {
            'test_r2': best_gcnn['test_r2'],
            'test_mse': best_gcnn['test_mse'],
            'train_r2': best_gcnn['train_r2'],
            'train_mse': best_gcnn['train_mse']
        }
    
    if not results:
        return
    
    # Figure 1: Test R² and MSE comparison
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Model Performance Comparison', fontsize=16, fontweight='bold', y=1.0)
    
    models = list(results.keys())
    test_r2_values = [results[m]['test_r2'] for m in models]
    test_mse_values = [results[m]['test_mse'] for m in models]
    
    # Color mapping
    colors = []
    for m in models:
        if 'CNN' in m and 'GCNN' not in m:
            colors.append(COLORS['cnn'])
        elif 'GCNN' in m:
            colors.append(COLORS['gcnn'])
        else:
            colors.append(COLORS['shallow'])
    
    # Test R²
    ax1 = axes[0]
    bars1 = ax1.barh(models, test_r2_values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax1.set_xlabel('Test R² Score', fontweight='bold', fontsize=12)
    ax1.set_title('(a) Test R² Comparison', fontweight='bold', fontsize=13)
    ax1.grid(axis='x', alpha=0.3, linestyle='--')
    ax1.set_xlim(left=0)
    
    # Add value labels
    for bar, val in zip(bars1, test_r2_values):
        width = bar.get_width()
        ax1.text(width, bar.get_y() + bar.get_height()/2, 
                f'{val:.4f}', ha='left', va='center', fontweight='bold', fontsize=10)
    
    # Test MSE
    ax2 = axes[1]
    bars2 = ax2.barh(models, test_mse_values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax2.set_xlabel('Test MSE', fontweight='bold', fontsize=12)
    ax2.set_title('(b) Test MSE Comparison', fontweight='bold', fontsize=13)
    ax2.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add value labels
    for bar, val in zip(bars2, test_mse_values):
        width = bar.get_width()
        ax2.text(width, bar.get_y() + bar.get_height()/2, 
                f'{val:.4f}', ha='left', va='center', fontweight='bold', fontsize=10)
    
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.savefig('combined_comparison_metrics.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Saved combined_comparison_metrics.png")
    plt.close()
    
    # Figure 2: Training curves comparison
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Training Progress Comparison', fontsize=16, fontweight='bold', y=1.0)
    
    # Test R² over epochs
    ax1 = axes[0]
    if cnn_df is not None:
        ax1.plot(cnn_df['epoch'], cnn_df['test_r2'], label='CNN', 
                color=COLORS['cnn'], linewidth=2.5, alpha=0.8)
    if gcnn_df is not None:
        ax1.plot(gcnn_df['epoch'], gcnn_df['test_r2'], label='GCNN', 
                color=COLORS['gcnn'], linewidth=2.5, alpha=0.8)
    if shallow_df is not None and len(shallow_df) > 0:
        for _, row in shallow_df.iterrows():
            # Shallow methods are single points, plot as horizontal line
            ax1.axhline(y=row['test_r2_mean'], label=f"Shallow ({row['model']})", 
                       color=COLORS['shallow'], linestyle='--', linewidth=2, alpha=0.8)
    ax1.set_xlabel('Epoch', fontweight='bold', fontsize=12)
    ax1.set_ylabel('Test R² Score', fontweight='bold', fontsize=12)
    ax1.set_title('(a) Test R² vs Epoch', fontweight='bold', fontsize=13)
    ax1.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # Test Loss/MSE over epochs
    ax2 = axes[1]
    if cnn_df is not None:
        ax2.plot(cnn_df['epoch'], cnn_df['test_loss'], label='CNN', 
                color=COLORS['cnn'], linewidth=2.5, alpha=0.8)
    if gcnn_df is not None:
        ax2.plot(gcnn_df['epoch'], gcnn_df['test_mse'], label='GCNN', 
                color=COLORS['gcnn'], linewidth=2.5, alpha=0.8)
    if shallow_df is not None and len(shallow_df) > 0:
        for _, row in shallow_df.iterrows():
            ax2.axhline(y=row['test_mse_mean'], label=f"Shallow ({row['model']})", 
                       color=COLORS['shallow'], linestyle='--', linewidth=2, alpha=0.8)
    ax2.set_xlabel('Epoch', fontweight='bold', fontsize=12)
    ax2.set_ylabel('Test Loss/MSE', fontweight='bold', fontsize=12)
    ax2.set_title('(b) Test Loss/MSE vs Epoch', fontweight='bold', fontsize=13)
    ax2.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.savefig('combined_training_curves.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Saved combined_training_curves.png")
    plt.close()
    
    # Figure 3: Comprehensive comparison table visualization
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')
    
    # Prepare table data
    table_data = []
    headers = ['Model', 'Test R²', 'Test MSE', 'Train R²', 'Train MSE']
    
    for model, metrics in results.items():
        table_data.append([
            model,
            f"{metrics['test_r2']:.4f}",
            f"{metrics['test_mse']:.4f}",
            f"{metrics['train_r2']:.4f}",
            f"{metrics['train_mse']:.4f}"
        ])
    
    table = ax.table(cellText=table_data, colLabels=headers, 
                    cellLoc='center', loc='center',
                    bbox=[0, 0, 1, 1])
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)
    
    # Style header
    for i in range(len(headers)):
        table[(0, i)].set_facecolor('#4A90E2')
        table[(0, i)].set_text_props(weight='bold', color='white')
        table[(0, i)].set_height(0.1)
    
    # Style rows
    for i, model in enumerate(models, 1):
        color = colors[i-1] if i <= len(colors) else '#FFFFFF'
        for j in range(len(headers)):
            table[(i, j)].set_facecolor(color)
            table[(i, j)].set_alpha(0.7)
            if j == 0:
                table[(i, j)].set_text_props(weight='bold')
    
    plt.title('Comprehensive Model Performance Summary', 
             fontsize=16, fontweight='bold', pad=20)
    plt.savefig('combined_performance_table.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Saved combined_performance_table.png")
    plt.close()

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main function to generate all visualizations"""
    print("=" * 70)
    print("Generating Research Paper Quality Visualizations")
    print("=" * 70)
    
    # Load data
    print("\n[1/6] Loading CNN results...")
    cnn_df = load_cnn_results()
    
    print("\n[2/6] Loading Shallow Methods results...")
    shallow_df = load_shallow_methods_results()
    
    print("\n[3/6] Loading GCNN results...")
    gcnn_df, gcnn_data = load_gcnn_results()
    
    # Individual visualizations
    print("\n[4/6] Creating individual CNN visualizations...")
    visualize_cnn_individual(cnn_df)
    
    print("\n[5/6] Creating individual Shallow Methods visualizations...")
    visualize_shallow_methods_individual(shallow_df)
    
    print("\n[6/6] Creating individual GCNN visualizations...")
    visualize_gcnn_individual(gcnn_df, gcnn_data)
    
    # Combined visualizations
    print("\n[7/7] Creating combined comparison visualizations...")
    visualize_combined_comparison(cnn_df, shallow_df, gcnn_df)
    
    print("\n" + "=" * 70)
    print("Visualization Complete!")
    print("=" * 70)
    print("\nGenerated Files:")
    print("  Individual Visualizations:")
    if cnn_df is not None:
        print("    - cnn_individual_results.png")
    if shallow_df is not None:
        print("    - shallow_methods_individual_results.png")
    if gcnn_df is not None:
        print("    - gcnn_individual_results.png")
        print("    - gcnn_predictions_scatter.png")
    print("  Combined Visualizations:")
    print("    - combined_comparison_metrics.png")
    print("    - combined_training_curves.png")
    print("    - combined_performance_table.png")
    print("=" * 70)

if __name__ == "__main__":
    main()

