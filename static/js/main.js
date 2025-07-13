// Main JavaScript file for Military Unit Dashboard

// Enable Bootstrap tooltips
document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Enable Bootstrap popovers
document.addEventListener('DOMContentLoaded', function() {
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});

// Dynamically populate Rank options based on selected Branch
// Mapping of branch to rank lists – keep in sync with models.Soldier constants
const BRANCH_RANKS = {
    "Army": [
        "Private","Private First Class","Specialist","Corporal","Sergeant","Staff Sergeant","Sergeant First Class","Master Sergeant","First Sergeant","Sergeant Major","Command Sergeant Major","Sergeant Major of the Army","Warrant Officer 1","Chief Warrant Officer 2","Chief Warrant Officer 3","Chief Warrant Officer 4","Chief Warrant Officer 5","Second Lieutenant","First Lieutenant","Captain","Major","Lieutenant Colonel","Colonel","Brigadier General","Major General","Lieutenant General","General","General of the Army"
    ],
    "Navy": [
        "Seaman Recruit","Seaman Apprentice","Seaman","Petty Officer Third Class","Petty Officer Second Class","Petty Officer First Class","Chief Petty Officer","Senior Chief Petty Officer","Master Chief Petty Officer","Command Master Chief Petty Officer","Fleet/Force Master Chief Petty Officer","Master Chief Petty Officer of the Navy","Ensign","Lieutenant Junior Grade","Lieutenant","Lieutenant Commander","Commander","Captain","Rear Admiral Lower Half","Rear Admiral Upper Half","Vice Admiral","Admiral","Fleet Admiral"
    ],
    "Air Force": [
        "Airman Basic","Airman","Airman First Class","Senior Airman","Staff Sergeant","Technical Sergeant","Master Sergeant","Senior Master Sergeant","Chief Master Sergeant","Command Chief Master Sergeant","Chief Master Sergeant of the Air Force","Second Lieutenant","First Lieutenant","Captain","Major","Lieutenant Colonel","Colonel","Brigadier General","Major General","Lieutenant General","General","General of the Air Force"
    ],
    "Marine Corps": [
        "Private","Private First Class","Lance Corporal","Corporal","Sergeant","Staff Sergeant","Gunnery Sergeant","Master Sergeant","First Sergeant","Master Gunnery Sergeant","Sergeant Major","Sergeant Major of the Marine Corps","Second Lieutenant","First Lieutenant","Captain","Major","Lieutenant Colonel","Colonel","Brigadier General","Major General","Lieutenant General","General","Commandant of the Marine Corps"
    ],
    "Coast Guard": [
        "Seaman Recruit","Seaman Apprentice","Seaman","Petty Officer Third Class","Petty Officer Second Class","Petty Officer First Class","Chief Petty Officer","Senior Chief Petty Officer","Master Chief Petty Officer","Command Master Chief Petty Officer","District Master Chief Petty Officer","Area Master Chief Petty Officer","Master Chief Petty Officer of the Coast Guard","Ensign","Lieutenant Junior Grade","Lieutenant","Lieutenant Commander","Commander","Captain","Rear Admiral Lower Half","Rear Admiral Upper Half","Vice Admiral","Admiral"
    ]
};

document.addEventListener('DOMContentLoaded', function() {
    const branchSelect = document.getElementById('id_branch');
    const rankSelect = document.getElementById('id_rank');

    if (branchSelect && rankSelect) {
        const populateRanks = (branch) => {
            const ranks = BRANCH_RANKS[branch] || [];
            // Clear existing options
            rankSelect.innerHTML = '';
            // Add placeholder
            const ph = document.createElement('option');
            ph.value = '';
            ph.textContent = '--- Select Rank ---';
            rankSelect.appendChild(ph);
            // Populate options
            ranks.forEach(r => {
                const opt = document.createElement('option');
                opt.value = r;
                opt.textContent = r;
                rankSelect.appendChild(opt);
            });
        };

        // Initial population based on default branch value
        populateRanks(branchSelect.value);

        branchSelect.addEventListener('change', (e) => {
            populateRanks(e.target.value);
        });
    }
});

// Confirm delete actions
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-confirm');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
});
