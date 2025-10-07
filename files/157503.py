<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="Lenovo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 11:42:28 AM"/>
        <attribute name="created" value="TGVub3ZvO0xBUFRPUC1GMk9BVDRQSTsyNTY4LTA3LTIwOzExOjI3OjE3IEFNOzI5Njc="/>
        <attribute name="edited" value="TGVub3ZvO0xBUFRPUC1GMk9BVDRQSTsyNTY4LTA3LTIwOzExOjQyOjI4IEFNOzE7MzA3NA=="/>
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