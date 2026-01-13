# Visualization Folder

This folder contains visualization scripts and generated output images for the research project.

## Scripts

1. **`visualize_all_results.py`** - Comprehensive visualization script that generates:
   - Individual visualizations for CNN, Shallow Methods, and GCNN
   - Combined comparison visualizations
   - Research paper quality plots with proper formatting

2. **`visualize_results.py`** - Original visualization script for shallow methods and GCNN results

## Usage

Run the scripts from the parent directory (baseline/) or from within this folder:

```bash
# From parent directory
python visualization/visualize_all_results.py

# Or from within visualization folder
cd visualization
python visualize_all_results.py
```

## Output Files

### Individual Method Visualizations
- `cnn_individual_results.png` - CNN training progress and metrics
- `shallow_methods_individual_results.png` - Shallow learning methods comparison
- `gcnn_individual_results.png` - GCNN training progress and metrics
- `gcnn_predictions_scatter.png` - GCNN prediction vs actual scatter plots

### Combined Comparison Visualizations
- `combined_comparison_metrics.png` - Side-by-side comparison of all methods
- `combined_training_curves.png` - Training progress comparison across methods
- `combined_performance_table.png` - Comprehensive performance summary table

### Legacy Files
- `shallow_methods_comparison.png` - Original shallow methods comparison
- `gcnn_training_curves.png` - Original GCNN training curves
- `gcnn_predictions.png` - Original GCNN predictions
- `methods_comparison.png` - Original methods comparison

## Data Sources

The scripts load data from the parent directory:
- `../training_results_cnn.csv` - CNN training results
- `../results_shallow_methods.csv` - Shallow methods results
- `../results/` - GCNN prediction and actual value files

## Notes

- All visualizations are saved at 300 DPI for publication quality
- Scripts use research paper formatting (serif fonts, proper colors, etc.)
- Output files are saved directly in this folder

