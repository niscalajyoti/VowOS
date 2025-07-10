<?php
// Define the filename for the PDF and its counter
$pdfFile = 'The_Five_Vows-VowOS.pdf';
$counterFile = 'pdf_counter.txt';

// --- Increment Counter ---
// Check if the counter file exists. If not, create it.
if (!file_exists($counterFile)) {
    file_put_contents($counterFile, '0');
}
// Read the current count, increment it, and save it back
$count = (int)file_get_contents($counterFile);
$count++;
file_put_contents($counterFile, $count);

// --- Serve the File for Download ---
// Check that the PDF file actually exists before serving it
if (file_exists($pdfFile)) {
    // Set headers to force download
    header('Content-Description: File Transfer');
    header('Content-Type: application/pdf');
    header('Content-Disposition: attachment; filename="' . basename($pdfFile) . '"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($pdfFile));
    // Clear output buffer
    flush(); 
    // Read the file and send it to the output buffer
    readfile($pdfFile);
    exit;
}
?>
