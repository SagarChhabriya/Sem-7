"""
Visualization script for shallow methods and GCNN results
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
from pathlib import Path
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def load_shallow_methods_results():
    """Load and visualize shallow methods results"""
    csv_path = '../results_shallow_methods.csv'
    if not os.path.exists(csv_path):
        print("Warning: results_shallow_methods.csv not found")
        return None
    
    df = pd.read_csv(csv_path)
    print(f"Loaded shallow methods results: {len(df)} rows")
    print(df.head())
    return df

def visualize_shallow_methods(df):
    """Create visualizations for shallow methods"""
    if df is None or len(df) == 0:
        return
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Shallow Methods Performance Comparison', fontsize=16, fontweight='bold')
    
    # Extract model names
    models = df['model'].unique()
    colors = plt.cm.Set3(np.linspace(0, 1, len(models)))
    
    # 1. Test MSE Comparison
    ax1 = axes[0, 0]
    x_pos = np.arange(len(models))
    test_mse_means = [df[df['model'] == m]['test_mse_mean'].values[0] for m in models]
    test_mse_stds = [df[df['model'] == m]['test_mse_std'].values[0] for m in models]
    ax1.bar(x_pos, test_mse_means, yerr=test_mse_stds, capsize=5, color=colors, alpha=0.7, edgecolor='black')
    ax1.set_xlabel('Model')
    ax1.set_ylabel('Test MSE')
    ax1.set_title('Test MSE by Model')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(models, rotation=45, ha='right')
    ax1.grid(axis='y', alpha=0.3)
    
    # 2. Test R² Comparison
    ax2 = axes[0, 1]
    test_r2_means = [df[df['model'] == m]['test_r2_mean'].values[0] for m in models]
    test_r2_stds = [df[df['model'] == m]['test_r2_std'].values[0] for m in models]
    ax2.bar(x_pos, test_r2_means, yerr=test_r2_stds, capsize=5, color=colors, alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Model')
    ax2.set_ylabel('Test R²')
    ax2.set_title('Test R² by Model')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(models, rotation=45, ha='right')
    ax2.grid(axis='y', alpha=0.3)
    
    # 3. Train vs Test MSE
    ax3 = axes[1, 0]
    train_mse_means = [df[df['model'] == m]['train_mse_mean'].values[0] for m in models]
    x = np.arange(len(models))
    width = 0.35
    ax3.bar(x - width/2, train_mse_means, width, label='Train MSE', color='skyblue', alpha=0.7, edgecolor='black')
    ax3.bar(x + width/2, test_mse_means, width, label='Test MSE', color='lightcoral', alpha=0.7, edgecolor='black')
    ax3.set_xlabel('Model')
    ax3.set_ylabel('MSE')
    ax3.set_title('Train vs Test MSE')
    ax3.set_xticks(x)
    ax3.set_xticklabels(models, rotation=45, ha='right')
    ax3.legend()
    ax3.grid(axis='y', alpha=0.3)
    
    # 4. Train vs Test R²
    ax4 = axes[1, 1]
    train_r2_means = [df[df['model'] == m]['train_r2_mean'].values[0] for m in models]
    ax4.bar(x - width/2, train_r2_means, width, label='Train R²', color='lightgreen', alpha=0.7, edgecolor='black')
    ax4.bar(x + width/2, test_r2_means, width, label='Test R²', color='orange', alpha=0.7, edgecolor='black')
    ax4.set_xlabel('Model')
    ax4.set_ylabel('R²')
    ax4.set_title('Train vs Test R²')
    ax4.set_xticks(x)
    ax4.set_xticklabels(models, rotation=45, ha='right')
    ax4.legend()
    ax4.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('shallow_methods_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved shallow_methods_comparison.png")
    plt.close()

def extract_epoch_from_filename(filename):
    """Extract epoch number from filename"""
    match = re.search(r'epoch(\d+)', filename)
    return int(match.group(1)) if match else None

def load_gcnn_results():
    """Load GCNN results from results directory"""
    results_dir = Path('../results')
    if not results_dir.exists():
        print("Warning: results/ directory not found")
        return None
    
    # Find all epoch files
    epochs = set()
    for file in results_dir.glob('*.csv'):
        epoch = extract_epoch_from_filename(file.name)
        if epoch is not None:
            epochs.add(epoch)
    
    epochs = sorted(list(epochs))
    print(f"Found {len(epochs)} epochs: {epochs[:5]}...{epochs[-5:]}")
    
    # Load data for each epoch
    gcnn_data = []
    for epoch in epochs:
        try:
            pred_test = np.loadtxt(f'../results/gcnn_pred_test_m_epoch{epoch}.csv')
            actual_test = np.loadtxt(f'../results/gcnn_actual_test_m_epoch{epoch}.csv')
            pred_train = np.loadtxt(f'../results/gcnn_pred_train_m_epoch{epoch}.csv')
            actual_train = np.loadtxt(f'../results/gcnn_actual_train_m_epoch{epoch}.csv')
            
            # Calculate metrics
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
    
    return gcnn_data

def visualize_gcnn_training_curves(gcnn_data):
    """Visualize GCNN training progress over epochs"""
    if not gcnn_data:
        return
    
    df = pd.DataFrame([{k: v for k, v in d.items() if k not in ['pred_test', 'actual_test', 'pred_train', 'actual_train']} 
                       for d in gcnn_data])
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('GCNN Training Progress', fontsize=16, fontweight='bold')
    
    # 1. MSE over epochs
    ax1 = axes[0, 0]
    ax1.plot(df['epoch'], df['train_mse'], label='Train MSE', marker='o', markersize=3, linewidth=2)
    ax1.plot(df['epoch'], df['test_mse'], label='Test MSE', marker='s', markersize=3, linewidth=2)
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('MSE')
    ax1.set_title('MSE vs Epoch')
    ax1.legend()
    ax1.grid(alpha=0.3)
    
    # 2. R² over epochs
    ax2 = axes[0, 1]
    ax2.plot(df['epoch'], df['train_r2'], label='Train R²', marker='o', markersize=3, linewidth=2)
    ax2.plot(df['epoch'], df['test_r2'], label='Test R²', marker='s', markersize=3, linewidth=2)
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('R²')
    ax2.set_title('R² vs Epoch')
    ax2.legend()
    ax2.grid(alpha=0.3)
    
    # 3. MAE over epochs
    ax3 = axes[1, 0]
    ax3.plot(df['epoch'], df['train_mae'], label='Train MAE', marker='o', markersize=3, linewidth=2)
    ax3.plot(df['epoch'], df['test_mae'], label='Test MAE', marker='s', markersize=3, linewidth=2)
    ax3.set_xlabel('Epoch')
    ax3.set_ylabel('MAE')
    ax3.set_title('MAE vs Epoch')
    ax3.legend()
    ax3.grid(alpha=0.3)
    
    # 4. Best epoch summary
    ax4 = axes[1, 1]
    best_epoch_idx = df['test_r2'].idxmax()
    best_epoch = df.loc[best_epoch_idx]
    
    metrics = ['test_mse', 'test_r2', 'test_mae', 'train_mse', 'train_r2', 'train_mae']
    values = [best_epoch[m] for m in metrics]
    labels = [m.replace('_', ' ').title() for m in metrics]
    
    ax4.barh(labels, values, color=['skyblue' if 'test' in m else 'lightcoral' for m in metrics], alpha=0.7, edgecolor='black')
    ax4.set_xlabel('Value')
    ax4.set_title(f'Best Epoch ({int(best_epoch["epoch"])}) Metrics')
    ax4.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('gcnn_training_curves.png', dpi=300, bbox_inches='tight')
    print("Saved gcnn_training_curves.png")
    plt.close()

def visualize_gcnn_predictions(gcnn_data, epochs_to_plot=None):
    """Visualize predictions vs actuals for selected epochs"""
    if not gcnn_data:
        return
    
    if epochs_to_plot is None:
        # Plot first, middle, and last epochs
        epochs_to_plot = [
            gcnn_data[0]['epoch'],
            gcnn_data[len(gcnn_data)//2]['epoch'],
            gcnn_data[-1]['epoch']
        ]
    
    # Find data for selected epochs
    plot_data = [d for d in gcnn_data if d['epoch'] in epochs_to_plot]
    
    if not plot_data:
        return
    
    fig, axes = plt.subplots(len(plot_data), 2, figsize=(15, 5*len(plot_data)))
    if len(plot_data) == 1:
        axes = axes.reshape(1, -1)
    fig.suptitle('GCNN Predictions vs Actuals', fontsize=16, fontweight='bold')
    
    for idx, data in enumerate(plot_data):
        epoch = data['epoch']
        
        # Test set
        ax1 = axes[idx, 0]
        pred_test = data['pred_test']
        actual_test = data['actual_test']
        
        # Scatter plot
        ax1.scatter(actual_test, pred_test, alpha=0.5, s=10, edgecolors='black', linewidths=0.1)
        
        # Perfect prediction line
        min_val = min(actual_test.min(), pred_test.min())
        max_val = max(actual_test.max(), pred_test.max())
        ax1.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')
        
        ax1.set_xlabel('Actual')
        ax1.set_ylabel('Predicted')
        ax1.set_title(f'Test Set - Epoch {epoch} (R² = {data["test_r2"]:.4f})')
        ax1.legend()
        ax1.grid(alpha=0.3)
        
        # Train set
        ax2 = axes[idx, 1]
        pred_train = data['pred_train']
        actual_train = data['actual_train']
        
        ax2.scatter(actual_train, pred_train, alpha=0.5, s=10, edgecolors='black', linewidths=0.1)
        min_val = min(actual_train.min(), pred_train.min())
        max_val = max(actual_train.max(), pred_train.max())
        ax2.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')
        
        ax2.set_xlabel('Actual')
        ax2.set_ylabel('Predicted')
        ax2.set_title(f'Train Set - Epoch {epoch} (R² = {data["train_r2"]:.4f})')
        ax2.legend()
        ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('gcnn_predictions.png', dpi=300, bbox_inches='tight')
    print("Saved gcnn_predictions.png")
    plt.close()

def create_comparison_plot(shallow_df, gcnn_data):
    """Create a comparison plot between shallow methods and GCNN"""
    if shallow_df is None or not gcnn_data:
        return
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Shallow Methods vs GCNN Comparison', fontsize=16, fontweight='bold')
    
    # Get best GCNN results
    gcnn_df = pd.DataFrame([{k: v for k, v in d.items() if k not in ['pred_test', 'actual_test', 'pred_train', 'actual_train']} 
                            for d in gcnn_data])
    best_gcnn = gcnn_df.loc[gcnn_df['test_r2'].idxmax()]
    
    # Prepare data
    shallow_models = shallow_df['model'].tolist()
    shallow_test_r2 = shallow_df['test_r2_mean'].tolist()
    
    all_models = shallow_models + ['GCNN (Best)']
    all_r2 = shallow_test_r2 + [best_gcnn['test_r2']]
    
    # Test R² comparison
    ax1 = axes[0]
    colors = ['skyblue'] * len(shallow_models) + ['orange']
    bars = ax1.bar(range(len(all_models)), all_r2, color=colors, alpha=0.7, edgecolor='black')
    ax1.set_xlabel('Model')
    ax1.set_ylabel('Test R²')
    ax1.set_title('Test R² Comparison')
    ax1.set_xticks(range(len(all_models)))
    ax1.set_xticklabels(all_models, rotation=45, ha='right')
    ax1.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, (bar, val) in enumerate(zip(bars, all_r2)):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.4f}',
                ha='center', va='bottom', fontsize=9)
    
    # Test MSE comparison
    ax2 = axes[1]
    shallow_test_mse = shallow_df['test_mse_mean'].tolist()
    all_mse = shallow_test_mse + [best_gcnn['test_mse']]
    bars2 = ax2.bar(range(len(all_models)), all_mse, color=colors, alpha=0.7, edgecolor='black')
    ax2.set_xlabel('Model')
    ax2.set_ylabel('Test MSE')
    ax2.set_title('Test MSE Comparison')
    ax2.set_xticks(range(len(all_models)))
    ax2.set_xticklabels(all_models, rotation=45, ha='right')
    ax2.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, (bar, val) in enumerate(zip(bars2, all_mse)):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.4f}',
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig('methods_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved methods_comparison.png")
    plt.close()

def main():
    """Main function to run all visualizations"""
    print("=" * 60)
    print("Visualizing Results")
    print("=" * 60)
    
    # Visualize shallow methods
    print("\n1. Loading shallow methods results...")
    shallow_df = load_shallow_methods_results()
    if shallow_df is not None:
        print("2. Creating shallow methods visualizations...")
        visualize_shallow_methods(shallow_df)
    
    # Visualize GCNN results
    print("\n3. Loading GCNN results...")
    gcnn_data = load_gcnn_results()
    if gcnn_data:
        print("4. Creating GCNN training curves...")
        visualize_gcnn_training_curves(gcnn_data)
        
        print("5. Creating GCNN prediction plots...")
        visualize_gcnn_predictions(gcnn_data)
        
        # Comparison plot
        if shallow_df is not None:
            print("6. Creating comparison plot...")
            create_comparison_plot(shallow_df, gcnn_data)
    
    print("\n" + "=" * 60)
    print("Visualization complete!")
    print("Generated files:")
    if shallow_df is not None:
        print("  - shallow_methods_comparison.png")
    if gcnn_data:
        print("  - gcnn_training_curves.png")
        print("  - gcnn_predictions.png")
    if shallow_df is not None and gcnn_data:
        print("  - methods_comparison.png")
    print("=" * 60)

if __name__ == "__main__":
    main()

