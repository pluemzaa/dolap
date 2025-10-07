<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="print_numbers_flowgorithm"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 06:18:08 PM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLVFDUzFGUUE7MjU2OC0wNy0xNzswNjoxNToyOSBQTTsyNzk3"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLVFDUzFGUUE7MjU2OC0wNy0xNzswNjoxODowOCBQTTsxOzI5MDU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <for variable="i" start="start" end="end" direction="inc" step="1">
                <output expression="i" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>