<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="1-683380471-6"/>
        <attribute name="authors" value="HP"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 08:43:20 PM"/>
        <attribute name="created" value="SFA7V0lOMTE7MjU2OC0wNy0yMDswODoyOTo0NyBQTTsxNzky"/>
        <attribute name="edited" value="SFA7V0lOMTE7MjU2OC0wNy0yMDswODo0MzoyMCBQTTsxOzE4ODc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="startnum, endnum, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="startnum"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="endnum"/>
            <for variable="i" start="startnum" end="endnum" direction="inc" step="1">
                <output expression="i" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>