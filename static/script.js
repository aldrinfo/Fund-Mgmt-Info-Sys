// Function to show/hide filter options based on selected query
function showFilterOptions() {
    const queryType = document.getElementById('query_type').value;
    const filterOptions = document.getElementById('filter_options');
    
    // Hide all filters first
    document.querySelectorAll('#active_filters > div').forEach(div => {
        div.style.display = 'none';
    });
    
    if (queryType) {
        // Show different filters based on query type
        switch(queryType) {
            case 'total_sales_profit':
                // Show all filters for comprehensive analysis
                document.getElementById('category_filter').style.display = 'block';
                document.getElementById('subcategory_filter').style.display = 'block';
                document.getElementById('segment_filter').style.display = 'block';
                document.getElementById('region_filter').style.display = 'block';
                document.getElementById('year_filter').style.display = 'block';
                break;
                
            case 'avg_discount_product':
                // Only show category and subcategory filters
                document.getElementById('category_filter').style.display = 'block';
                document.getElementById('subcategory_filter').style.display = 'block';
                break;
                
            case 'sales_by_year':
                // Already grouped by year, so show other relevant filters
                document.getElementById('category_filter').style.display = 'block';
                document.getElementById('subcategory_filter').style.display = 'block';
                document.getElementById('segment_filter').style.display = 'block';
                document.getElementById('region_filter').style.display = 'block';
                break;
                
            case 'profit_by_region':
                // Already grouped by region, so show other relevant filters
                document.getElementById('category_filter').style.display = 'block';
                document.getElementById('subcategory_filter').style.display = 'block';
                document.getElementById('segment_filter').style.display = 'block';
                document.getElementById('year_filter').style.display = 'block';
                break;
                
            case 'negative_profit':
                // Only show product-related filters
                document.getElementById('category_filter').style.display = 'block';
                document.getElementById('subcategory_filter').style.display = 'block';
                break;
        }
    }
}

// Function to toggle individual filters
function toggleFilter(filterId, show) {
    const filterElement = document.getElementById(filterId);
    filterElement.style.display = show ? 'block' : 'none';
    
    // Handle dependencies between filters
    if (filterId === 'subcategory_filter' && show) {
        // If showing subcategory, ensure category is also shown
        document.getElementById('category_filter').style.display = 'block';
        document.getElementById('use_category').checked = true;
    }
    
    // If hiding category, also hide subcategory
    if (filterId === 'category_filter' && !show) {
        document.getElementById('subcategory_filter').style.display = 'none';
        document.getElementById('use_subcategory').checked = false;
    }
}

// Optional: Add function to update subcategories based on selected category
function updateSubcategories() {
    const categorySelect = document.getElementById('category');
    const subcategorySelect = document.getElementById('sub_category');
    const selectedCategory = categorySelect.value;
    
    // You would need to implement this part based on your data structure
    // This would filter subcategories based on the selected category
}