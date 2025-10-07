<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="testtt"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 08:31:51 PM"/>
        <attribute name="created" value="dG9ud2E7REVTS1RPUC04N0hRN1BBOzIwMjUtMDctMTY7MDg6Mjk6MDggUE07Mjg5NA=="/>
        <attribute name="edited" value="dG9ud2E7REVTS1RPUC04N0hRN1BBOzIwMjUtMDctMTY7MDg6MzE6NTEgUE07MjsyOTk0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="startNum, endNum, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="startNum"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="endNum"/>
            <for variable="i" start="startNum" end="endNum" direction="inc" step="1">
                <output expression="ToString(i)" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>