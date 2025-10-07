<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flow"/>
        <attribute name="authors" value="TUF Gaming F15"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 10:53:47 PM"/>
        <attribute name="created" value="VFVGIEdhbWluZyBGMTU7REVTS1RPUC03UFBINkxWOzI1NjgtMDctMTk7MTA6NDc6NTkgUE07MzQ2NA=="/>
        <attribute name="edited" value="VFVGIEdhbWluZyBGMTU7REVTS1RPUC03UFBINkxWOzI1NjgtMDctMTk7MTA6NTM6NDcgUE07MTszNTY2"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="startNum, endNum, i" type="Integer" array="False" size=""/>
            <output expression="&quot;input start number: &quot;" newline="True"/>
            <input variable="startNum"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="endNum"/>
            <assign variable="i" expression="startNum"/>
            <while expression="i &lt;= endNum">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>